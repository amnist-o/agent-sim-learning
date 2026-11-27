# Lesson 01: Your First Mesa 3 Model — Strategic Ad Competition

Welcome to **Lesson 01**! In Lesson 00, you built a one-period market engine in `numpy` where both channels' ad loads were frozen. Now you will turn that market into a live **Agent-Based Model (ABM)** in **Mesa 3**, where both broadcasters actively adjust their ad loads period by period until the market settles into equilibrium.

* **`README.md`** (this file): The economic setup, plain-language guide to Python classes and Mesa 3, your coding tasks, and verification numbers.
* **`work.py`**: Your workspace where **you** write the complete code.
* **Redoing later:** Create a new file like `redo_1.py` in this folder anytime you want fresh practice.

---

## 1. Economic Setup (Dynamic Stage 2 of Peitz & Valletti, 2008)

We keep the exact same Free-TV duopoly from Lesson 00:
* **Viewers:** `N = 1001` households evenly spaced on `[0, 1]` (`beta = np.linspace(0.0, 1.0, 1001)`).
* **Baseline Parameters:** `V = 10.0`, `delta = 0.5`, `t = 4.0`, `r = 0.40`, `F = 0.50`, `u_off = 0.0`.
* **Two Broadcaster Agents (fixed genres, adjustable ads):**
  * **Channel 0:** genre `d = 0.25`, starting ad load `a = 6.0`.
  * **Channel 1:** genre `d = 0.75`, starting ad load `a = 8.0`.
* **Why keep viewers as a `numpy` array and make broadcasters Mesa `Agent`s?**
  Right now, all 1,001 viewers simply pick the highest-utility option with no memory or learning. Keeping them in one vectorized `numpy` array inside the `Model` is ~50x faster than creating 1,001 Python objects, while the two **Broadcasters** are genuine strategic `Agent`s that hold state (`d`, `a`, `share`, `profit`) and take actions each period. (We will add adaptive/heterogeneous viewer agents in later lessons!)

### Broadcaster Behavior Rule (Myopic Local Adjustment)
In each period `t = 1, 2, ..., T`, each broadcaster takes a turn trying to raise its own profit:
1. It tests three nearby ad loads: **`a - step_size`**, **`a`** (stay put), and **`a + step_size`** (with `step_size = 0.5`), staying within legal bounds **`[0.0, a_max]`** (baseline `a_max = 12.0`).
2. Holding the rival channel's current ad load fixed, it calculates what its own profit would be at each of those three candidate ad loads.
3. It updates its ad load `a` to whichever candidate gives the **highest profit**.
4. After both broadcasters move, the model recomputes the market outcome (`share`, `profit`, `cs`, `welfare`) and records a snapshot using Mesa's **`DataCollector`**.

### Analytical Benchmark (Pen-and-Paper Nash Equilibrium)
With `d_0 = 0.25` and `d_1 = 0.75`, setting $U_0(\hat{\beta}) = U_1(\hat{\beta})$ gives Channel 0's share $D_0 = 0.5 + \frac{a_1 - a_0}{8}$. Maximizing $\pi_0 = r a_0 D_0 - F$ gives the best-response rule:
$$a_0^*(a_1) = 2 + \frac{a_1}{2}, \qquad a_1^*(a_0) = 2 + \frac{a_0}{2}$$
Solving both together pins down the unique Nash Equilibrium: **$a_0^* = a_1^* = 4.0$**. Your agent-based simulation should converge right onto this equilibrium!

---

## 2. Plain-Language Guide to Python Classes & Mesa 3

*(None of the snippets below solve your TV assignment — they use a tiny coffee-shop example to show the exact Mesa 3 mechanics.)*

### A. What is a `class` and what is `self`?
Think of a **`class`** as a **blueprint** (like a template for an economic agent or a market):
* `def __init__(self, ...):` runs once when a new agent or model is created, setting its starting attributes (like `self.price = 5.0`).
* **`self`** simply means *"this specific agent"* (or *"this specific model"*). Inside a `Shop` class, `self.price` is *this shop's* price, separate from another shop's `self.price`.
* **`super().__init__(...)`** runs Mesa's built-in setup first (in Mesa 3, this automatically assigns each agent a `unique_id` and registers it inside `model.agents`!).

### B. Minimal Mesa 3 Template (`Agent`, `Model`, `DataCollector`)
```python
import numpy as np
from mesa import Agent, Model
from mesa.datacollection import DataCollector


class CoffeeShop(Agent):
    def __init__(self, model, name, start_price):
        super().__init__(model)          # Registers this agent in model.agents
        self.name = name
        self.price = start_price
        self.profit = 0.0

    def step(self):
        # Test lowering, keeping, or raising price by 0.5 (within [1.0, 10.0])
        candidates = [
            max(1.0, min(self.model.p_max, self.price + dp))
            for dp in (-0.5, 0.0, 0.5)
        ]
        # Pick the candidate price that gives the highest profit
        self.price = max(
            candidates,
            key=lambda p: self.model.preview_profit(self, candidate_price=p),
        )


class CoffeeMarket(Model):
    def __init__(self, p_max=10.0, seed=42):
        super().__init__(seed=seed)      # Always call this first in Mesa 3!
        self.p_max = p_max
        self.customers = np.linspace(0.0, 1.0, 101)

        # Create agents (Mesa automatically adds them to self.agents)
        self.shop_0 = CoffeeShop(self, name="Shop 0", start_price=6.0)
        self.shop_1 = CoffeeShop(self, name="Shop 1", start_price=8.0)

        self.avg_surplus = 0.0

        # DataCollector records a table of results every time we call .collect(self)
        self.datacollector = DataCollector(
            model_reporters={
                "p_0": lambda m: m.shop_0.price,
                "p_1": lambda m: m.shop_1.price,
                "avg_surplus": lambda m: m.avg_surplus,
            }
        )

    def preview_profit(self, shop, candidate_price):
        # Compute what `shop` would earn if it charged `candidate_price`
        ...

    def update_market(self):
        # Compute shares, profits, and avg_surplus at current prices
        ...

    def step(self):
        self.agents.do("step")           # Runs .step() on each agent in order
        self.update_market()             # Updates shares, profits, surplus
        self.datacollector.collect(self) # Saves one row to the history table
```

### C. Running the Model & Reading the Collected Table (`pandas` DataFrame)
```python
model = CoffeeMarket(p_max=10.0)
for _ in range(15):
    model.step()

# Convert recorded history into a pandas table (just like an R data.frame!)
history = model.datacollector.get_model_vars_dataframe()
print(history.round(4))

# Grab the final row (like tail(history, 1) in R)
final_row = history.iloc[-1]
print(f"Final prices: {final_row['p_0']:.1f}, {final_row['p_1']:.1f}")
```

---

## 3. Your Coding Tasks (Write in `work.py`)

Write a clean, self-contained Mesa 3 script in [`work.py`](./work.py) that completes all three tasks:

1. **Task 1 — Build `Broadcaster(Agent)` and `TVMarketModel(Model)`:**
   * Create a `Broadcaster` agent class that stores `name`, `d` (genre location), `a` (current ad load), `share`, and `profit`, and implements `step()` using the myopic local adjustment rule (`step_size = 0.5`, bounded to `[0.0, self.model.a_max]`).
   * Create a `TVMarketModel` class with parameters `a_max=12.0`, `step_size=0.5`, `V=10.0`, `delta=0.5`, `t=4.0`, `r=0.40`, `F=0.50`, `u_off=0.0`, and `seed=42`.
   * Reuse your Lesson 00 vectorized viewer-choice math inside a helper method (so both `preview_profit` and `update_market` use the exact same market logic — zero duplicated formulas!).
   * Attach a `DataCollector` recording at least: `a_0`, `a_1`, `share_0`, `share_1`, `profit_0`, `profit_1`, `cs`, and `welfare`.

2. **Task 2 — Baseline Dynamic Run (`a_max = 12.0`, 15 periods):**
   * Run `TVMarketModel` for 15 periods starting from `(a_0 = 6.0, a_1 = 8.0)`.
   * Print the collected history table rounded to 4 decimal places (`history.round(4)`), and verify that both broadcasters converge to the Nash equilibrium `(a_0 = 4.0, a_1 = 4.0)`.

3. **Task 3 — Ad-Cap Policy Experiment (`a_max` in `[2.0, 3.0, 4.0, 6.0]`):**
   * Loop over `a_max` values `[2.0, 3.0, 4.0, 6.0]`, running a fresh `TVMarketModel(a_max=cap)` for 15 periods each.
   * Print a clean summary table showing each `a_max` alongside the final-period `a_0`, `a_1`, `profit_0`, `profit_1`, `cs`, and `welfare`.
   * Add a 2–3 line comment at the bottom explaining:
     1. When does the ad cap bind, and what happens to `welfare` vs. broadcaster `profit`?
     2. What real-world economic risk shows up at `a_max = 2.0` even though `welfare` looks highest?

---

## 4. Self-Check Verification Numbers

Before running on this machine, make sure `mesa` and `pandas` are installed in your Python environment (`pip install mesa pandas numpy matplotlib`, or use the project `.venv`).

When you run your **Task 2** baseline (`a_max = 12.0`, starting from `a_0 = 6.0, a_1 = 8.0`, sequential `self.agents.do("step")`), by period `t = 9` (and staying constant through `t = 15`) you should see:
* **`a_0 = 4.0`**, **`a_1 = 4.0`**
* **`share_0 = 0.5005`**, **`share_1 = 0.4995`**
* **`profit_0 = 0.3008`**, **`profit_1 = 0.2992`**
* **`cs = 7.9165`**, **`welfare = 8.5165`**

And in **Task 3** (`a_max = 2.0`), check that both `profit_0` and `profit_1` turn **negative** (`≈ -0.100`) even though `welfare ≈ 8.7165`!
