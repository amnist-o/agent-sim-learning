# Lesson 00: Python Warm-Up via Viewer Choice & Welfare
# Read `lessons/00_python_warmup/README.md` for the setup, syntax examples, and check-numbers.
# Write your complete code below, then tell me when you're ready for review!
import numpy as np

# set up parameters
beta = np.linspace(0, 1, 1001)
d_0 = 0.25
d_1 = 0.75
a_0 = 6
a_1 = 8

# make a function named evaluate_market with beta, d0, d1, a0, a1, V = 10, delta = 0.5, t = 4, r = 0.4, F = 0.5)
def evaluate_market(beta, d_0, d_1,a_0, a_1, u_off = 0,
                    V = 10, delta = 0.5, t = 4, r = 0.4, F = 0.5):
    u_0 = V-(delta*a_0)- t*((beta-d_0) ** 2)
    u_1 = V-(delta*a_1)- t*((beta-d_1) ** 2)
    choose_0 = (u_0 >= u_1) & (u_0 > u_off)
    choose_1 = (u_1 > u_0) & (u_1 > u_off)
    choose_off = (u_0 <= u_off) & (u_1 <= u_off)
    share_0 = np.mean(choose_0)
    share_1 = np.mean(choose_1)
    share_off = np.mean(choose_off)
    utility = np.maximum(np.maximum(u_0, u_1), u_off)
    cs = np.mean(utility)
    profit_0 = r*a_0*share_0 - F
    profit_1 = r*a_1*share_1 - F
    welfare = np.mean(utility) + profit_0 + profit_1
    return {"share_0": share_0, "share_1": share_1,
            "share_off": share_off, "cs": cs,
            "profit_0": profit_0, "profit_1": profit_1,
            "welfare": welfare, "a_1": a_1}

baseline = evaluate_market(beta, d_0=d_0, d_1=d_1, a_0=a_0, a_1=a_1)

for name, val in baseline.items():
    print(f"{name}: {val:.4f}")

#varying advert for channel 1 from 2 to 12 at 0.5 per step
a_step = np.linspace(2, 12, 21)
results = []

for a in a_step:
    out = evaluate_market(beta, d_0=d_0, d_1=d_1, a_0=a_0, a_1 = a)
    results.append(out)
    print(f"a_1 = {a:4.1f} | share of channel 1 = {out["share_1"]:7.4f} | "
          f"profit of channel 1 = {out["profit_1"]:7.4f} | "
          f"Consumer Surplus = {out["cs"]:7.4f} | Welfare = {out["welfare"]:7.4f}")


# find the best result for max profit and max welfare
best_profit = max(results, key=lambda x: x["profit_1"])
best_welfare = max(results, key=lambda x: x["welfare"])
print(f"profit maxing ads: {best_profit['a_1']:4.1f} | "
      f"profit: {best_profit['profit_1']:7.4f} | "
      f"welfare maxing ads: {best_welfare['a_1']:4.1f} | "
      f"welfare: {best_welfare['welfare']:7.4f}")

# the results show that the ads level for max profit is at 5 while ads level for max welfare is at 4.5
# the ads level differ since it influences 2 things contradictly; viewers and ads profit
# while it increases profit per view, it also decreases viewers. Hence, the max profit is a spot where the reduction in viewers worth the marginal profit.
# Welfare measure not just the profit but consumer's utility as well. hence, ads for maximum welfare is less than ads for maximum profit.
# this simulation reflects that producers' benefit is not always public benefits even though welfare is composed of producers surplus as well.
# simulation with more depth can simulate the effect of policies to give a guideline on welfare, consumers, and producers surplus.