# Lesson 00: Python Warm-Up via Viewer Choice & Welfare

Welcome to **Lesson 00**! Every lesson folder in this project is self-contained so you can revisit or redo it months from now:
* **`README.md`** (this file): The economic setup, Python building-block examples, your coding assignment, and check-numbers to verify your results.
* **`work.py`**: Your workspace where **you** write the complete code.
* **Redoing later:** Anytime you want fresh practice without overwriting your finished `work.py`, simply create a new file like `redo_1.py` in this same folder and run that instead.

---

## 1. Economic Setup (From Peitz & Valletti, 2008)

Before introducing `Mesa` in Lesson 01, you will build the core **one-period market engine** of a Free-to-Air TV duopoly in pure Python + `numpy`.

* **Viewers:** `N = 1001` households evenly spaced along the taste interval `[0, 1]`, so viewer tastes are $\beta \in \{0.000, 0.001, \dots, 1.000\}$.
* **Outside Option (Turning the TV Off):** Gives utility `0.0`.
* **Two Free-TV Channels (`0` and `1`):**
  * Channel `0` airs content at taste location $d_0 = 0.25$ with ad minutes $a_0 = 6.0$.
  * Channel `1` airs content at taste location $d_1 = 0.75$ with ad minutes $a_1 = 8.0$.
* **Viewer Utility Formula:** A viewer with taste $\beta$ gets utility from Channel $i \in \{0, 1\}$:
  $$U_i(\beta) = V - \delta a_i - t(\beta - d_i)^2$$
  with baseline parameters:
  * $V = 10.0$ (base enjoyment of TV)
  * $\delta = 0.5$ (viewer annoyance per ad minute)
  * $t = 4.0$ (quadratic taste-mismatch penalty)
* **Viewer Choice & Tie-Breaking Rule (Crucial ABM Habit!):**
  * Each viewer watches whichever option gives the highest utility among `{Channel 0, Channel 1, TV Off (0.0)}`.
  * **Explicit tie-breaking:** 1) A viewer watches TV (instead of turning it off) if their best channel utility is `>= 0.0`. 2) If $U_0(\beta) = U_1(\beta)$ (exact tie between the two channels), the viewer chooses **Channel 0**.
* **Broadcaster Profit & Social Welfare (Normalized per Viewer so `N` Scales Cleanly):**
  * Audience share of Channel $i$: $D_i = \text{(number of viewers watching Channel } i\text{)} / N$.
  * Broadcaster $i$'s profit per capita:
    $$\pi_i = r \cdot a_i \cdot D_i - F$$
    where $r = 0.40$ (ad revenue per ad-minute per unit of market share) and $F = 0.50$ (fixed show cost).
  * **Consumer Surplus ($CS$):** Average realized utility across all `N` viewers.
  * **Total Social Welfare ($W$):**
    $$W = CS + \pi_0 + \pi_1$$
    *(Note: Here we treat `r` as the net value created per ad-viewer exposure captured by broadcasters, keeping advertisers passive just as in our baseline discussion).*

---

## 2. Python Syntax Building Blocks (Study These Examples)

*(See also [`docs/r_to_python_cheatsheet.md`](../../docs/r_to_python_cheatsheet.md) for side-by-side R comparisons. None of the snippets below solve your assignment—they show the mechanics so you can assemble the code yourself.)*

### A. Importing `numpy` & Creating Evenly Spaced Grids
```python
import numpy as np

# 5 evenly spaced points from 0.0 to 10.0 (inclusive)
x = np.linspace(0.0, 10.0, 5)          # array([0. , 2.5, 5. , 7.5, 10.])
cost = 2.0 * ((x - 3.0) ** 2)          # Note: ** is power in Python, NOT ^
```

### B. Boolean Masks (Logical Vectors) & Counting Shares
In `numpy`, `&` means element-wise AND, `|` means element-wise OR, and `~` means NOT. **Always wrap each comparison in parentheses `( )`!**
```python
val_a = np.array([3.0, 5.0, -1.0, 5.0])
val_b = np.array([2.0, 6.0, -2.0, 5.0])

# Pick A if A >= B AND A >= 0
choose_a = (val_a >= val_b) & (val_a >= 0.0)   # [True, False, False, True]
choose_b = (val_b > val_a) & (val_b >= 0.0)    # [False, True, False, False]

share_a = np.mean(choose_a)                    # 0.50 (mean of True/False = share!)
realized = np.maximum(np.maximum(val_a, val_b), 0.0)
```

### C. Writing a Function Returning a Dictionary & Finding the Best Grid Point
```python
def calc_revenue(price, slope=2.0):
    demand = max(0.0, 20.0 - slope * price)
    return {"price": price, "demand": demand, "rev": price * demand}

candidates = np.linspace(1.0, 9.0, 9)   # 1.0, 2.0, ..., 9.0
results = []                            # Empty Python list to collect rows

for p in candidates:
    out = calc_revenue(p)
    results.append(out)                 # Add dictionary to the list
    print(f"p = {p:4.1f} | demand = {out['demand']:5.2f} | rev = {out['rev']:6.2f}")

# Find the dictionary in `results` with the highest 'rev':
best = max(results, key=lambda row: row["rev"])
print(f"Revenue-maximizing price: {best['price']:.1f}")
```

---

## 3. Your Coding Tasks (Write in `work.py`)

Write a clean, self-contained script in [`work.py`](./work.py) that completes all three tasks:

1. **Task 1 — Reusable Market Function:**
   Write a function `evaluate_market(beta, d0, d1, a0, a1, V=10.0, delta=0.5, t=4.0, r=0.40, F=0.50)` that uses **vectorized `numpy` array operations** (do *not* write a `for` loop over the 1,001 viewers!) to compute and return a dictionary with:
   * `"share_0"`, `"share_1"`, `"share_off"`
   * `"cs"` (average realized viewer utility across all `N` viewers)
   * `"profit_0"`, `"profit_1"`
   * `"welfare"` ($CS + \pi_0 + \pi_1$)

2. **Task 2 — Baseline Benchmark Check (`a0 = 6.0`, `a1 = 8.0`):**
   Create `beta` for `N = 1001` viewers on `[0, 1]`, call `evaluate_market` at the baseline (`d0 = 0.25, d1 = 0.75, a0 = 6.0, a1 = 8.0`), and print all returned metrics clearly rounded to 4 decimal places.

3. **Task 3 — Policy Sweep (`a1` from `2.0` to `12.0` in steps of `0.5`):**
   Holding Channel 0 fixed at `d0 = 0.25, a0 = 6.0` and Channel 1's genre at `d1 = 0.75`, loop over `a1` from `2.0` to `12.0` (step `0.5`, i.e., 21 values):
   * Print a formatted table showing `a1`, `share_1`, `profit_1`, `cs`, and `welfare`.
   * At the bottom, print:
     1. Which `a1` on the grid maximizes **Channel 1's private profit** (`profit_1`), and
     2. Which `a1` on the grid maximizes **Total Social Welfare** (`welfare`),
     plus a 1–2 line comment in your code explaining *why* those two ad levels differ economically!

---

## 4. Self-Check Verification Numbers (Did You Build It Right?)

When you run `.\.venv\Scripts\python.exe lessons\00_python_warmup\work.py`, your **Task 2** baseline (`a0 = 6.0, a1 = 8.0`) should match:
* By pen-and-paper algebra ($U_0(\hat{\beta}) = U_1(\hat{\beta})$), the indifferent viewer sits right at $\hat{\beta} = 0.7500$!
* Because viewer `#750` ($\beta = 0.750$) is an exact tie ($U_0 = 6.0, U_1 = 6.0$) and ties go to Channel 0:
  * `share_0` = `751 / 1001` $\approx$ **`0.7502`** (`0.75025`)
  * `share_1` = `250 / 1001` $\approx$ **`0.2498`** (`0.24975`)
  * `share_off` = **`0.0000`**
  * `profit_0` $\approx$ **`1.3006`**, `profit_1` $\approx$ **`0.2992`**
