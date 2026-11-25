# Python for R-Speaking Economists — Quick Reference

This cheat sheet translates everyday R habits into clean Python. Every time a new Python tool appears in a lesson, we add it here.

---

## 1. Running a Script

In the terminal (from the project root `d:\git\agent-sim-learning`):
```powershell
.\.venv\Scripts\python.exe lessons\00_python_warmup\work.py
```

---

## 2. Variables, Math, and Comments

* **Assignment:** Python uses `=` (never `<-`).
* **Exponents:** Python uses `**` for powers (NOT `^`! In Python, `^` means something completely different).
* **Comments:** `#` works the exact same way as in R.

```python
# R:      price <- 12.5; utility <- 10 - 0.5 * (price ^ 2)
price = 12.5
utility = 10.0 - 0.5 * (price ** 2)
```

---

## 3. Printing Clean Output (`f-strings`)

Instead of R's `paste0()` or `sprintf()`, Python puts an `f` right before the quotes and lets you drop variables inside `{ }`. Add `:.3f` inside `{ }` to round to 3 decimal places:

```python
share = 0.62541
profit = 14.2
print(f"Market share = {share:.3f}, Profit = {profit:.2f}")
# Output: Market share = 0.625, Profit = 14.20
```

---

## 4. Vectors / Arrays (`numpy`) and Counting From `0`

Base Python lists (`[1, 2, 3]`) do **not** do element-by-element math like R vectors! For R-style vector math, economists always import **`numpy`** (nicknamed `np`).

**CRITICAL DIFFERENCE — Indexing starts at `0`, not `1`:**
* In R, a vector of 5 items has positions `1, 2, 3, 4, 5`.
* In Python, a 5-item array has positions `0, 1, 2, 3, 4` (and `-1` grabs the last item).

```python
import numpy as np

# R:      income <- seq(0, 100, length.out = 5)
income = np.linspace(0.0, 100.0, 5)   # [0., 25., 50., 75., 100.]

# Element-by-element math (works just like R!)
tax = 0.20 * income
consumption = 5.0 + 0.8 * (income - tax)

# First element vs. last element
first_person = income[0]    # R: income[1]
last_person = income[-1]    # R: tail(income, 1)

# Summary stats (just like R's mean(), sum(), max())
avg_c = np.mean(consumption)
total_c = np.sum(consumption)
```

---

## 5. Element-Wise Comparisons & Choosing Between Options

In R, you use `ifelse(cond, a, b)` or `pmax(x, y)`. `numpy` has the exact same tools:

```python
import numpy as np

plan_a = np.array([4.0, 8.0, 2.0])
plan_b = np.array([5.0, 8.0, -1.0])

# Highest value at each position — R: pmax(plan_a, plan_b, 0)
best_val = np.maximum(np.maximum(plan_a, plan_b), 0.0)
# Result: [5.0, 8.0, 2.0]

# Conditional choice — R: ifelse(plan_a >= plan_b, "A", "B")
picked_a = (plan_a >= plan_b)         # Boolean array: [False, True, True]
share_a = np.mean(picked_a)           # True counts as 1, False as 0!
count_a = np.sum(picked_a)            # Total number of True entries
```

---

## 6. Indentation Instead of `{ }` (`if` and `for` Loops)

Python does **not** use curly braces `{ }`. Instead:
1. End the header line (`if ...:`, `for ...:`, `def ...:`) with a **colon `:`**.
2. Indent everything inside the block by **4 spaces**. When the indentation ends, the block ends!

```python
# R:      for (rate in c(0.01, 0.05, 0.10)) { ... }
rates = [0.01, 0.05, 0.10]

for rate in rates:
    payment = 1000 * rate
    if payment > 40:
        print(f"Rate {rate:.2f}: High payment ({payment:.1f})")
    else:
        print(f"Rate {rate:.2f}: Low payment ({payment:.1f})")
```

If you want a grid of numbers to loop over (like `seq(2, 10, by = 1)` in R):
* `range(5)` gives integers `0, 1, 2, 3, 4` (stops *before* 5!).
* `np.arange(2.0, 10.5, 1.0)` or `np.linspace(2.0, 10.0, 9)` gives clean numeric grids.

---

## 7. Writing Functions (`def`) & Returning Named Results (`dict`)

In R, a function returns multiple named numbers using `list(mean_y = m, total = s)`. In Python, the equivalent of a named list is a **dictionary** (`{"mean_y": m, "total": s}`):

```python
def summarize_tax(income_array, tax_rate=0.15):
    """Compute average tax and after-tax income."""
    taxes = tax_rate * income_array
    net_income = income_array - taxes
    return {
        "avg_tax": float(np.mean(taxes)),
        "avg_net": float(np.mean(net_income)),
    }

# Calling the function and reading a named result:
res = summarize_tax(income, tax_rate=0.20)
print(res["avg_net"])     # R equivalent: res$avg_net
```
