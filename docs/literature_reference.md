# Free-TV & Broadcasting Social Welfare — Literature Reference

*Saved from our earlier literature review conversation (`0e24c89f-d440-47d6-ae25-e935fc43f3f7`) so all verified citations, mathematical setups, and empirical benchmarks stay right inside this project.*

---

## 1. Core Theoretical Models (Our Simulation Building Blocks)

### Paper 1: Spence & Owen (1977) — Program Diversity & Niche Bias
* **Citation:** Spence, A. M., & Owen, B. M. (1977). *"Television Programming, Monopolistic Competition, and Welfare."* *The Quarterly Journal of Economics*, 91(1), 103–126. (Top-5 economics journal).
* **Core Setup:**
  * Viewer utility over programs $i = 1, \dots, n$ and outside numeraire good $y$:
    $$U = u(x_1, \dots, x_n) + y$$
  * Program cost: $C(x_i) = F_i + c_i x_i$, with fixed production cost $F_i > 0$ and marginal cost per extra viewer $c_i \approx 0$.
  * Social welfare:
    $$W = \sum_i \left[ \int_0^{x_i} P_i(s, x_{-i})\,ds - (F_i + c_i x_i) \right]$$
* **Key Welfare Insight:** Because serving an extra viewer costs $c_i \approx 0$, Pay TV creates an *intensive-margin* deadweight loss by pricing out viewers ($p_i > 0$). However, advertiser-supported Free TV pays broadcasters based on *headcount* rather than *intensity of preference*, causing an *extensive-margin* welfare loss: wasteful duplication of mass-appeal shows and under-provision of high-value niche or high-fixed-cost shows.

---

### Paper 2: Anderson & Coate (2005) — Two-Sided Broadcasting & Ad Nuisance
* **Citation:** Anderson, S. P., & Coate, S. (2005). *"Market Provision of Broadcasting: A Welfare Analysis."* *The Review of Economic Studies*, 72(4), 947–972. (Top-5 economics journal).
* **Core Setup:**
  * Linear Hotelling viewer utility on `[0, 1]` for platform $i$ at location $d_i$:
    $$U_i(x) = V - t|x - d_i| - \gamma a_i - p_i$$
    where $t$ is taste-mismatch cost, $\gamma$ is viewer nuisance per ad, $a_i$ is ad quantity, and $p_i$ is subscription price ($p_i = 0$ on Free TV).
  * Advertiser revenue per viewer: $R(a_i)$ (downward-sloping marginal advertiser willingness to pay).
  * Platform profit with audience share $s_i$:
    $$\pi_i = s_i \big[ p_i + R(a_i) \big] - F$$
  * Total Social Welfare $W$: Sum of viewer surplus + broadcaster profits + net advertiser surplus.
* **Key Welfare Insight:** Free-to-air competition can produce *either too many or too few* ads and programs depending on ad nuisance $\gamma$ vs. advertiser value, and allowing Pay-TV pricing can sometimes *reduce* total social welfare.

---

### Paper 3: Peitz & Valletti (2008) — Free-to-Air vs. Pay-TV Positioning
* **Citation:** Peitz, M., & Valletti, T. (2008). *"Content and Advertising in the Media: Pay-TV versus Free-to-Air."* *International Journal of Industrial Organization*, 26(4), 949–965. (Flagship Q1 IO field journal).
* **Core Setup (Our Initial Simulation Anchor):**
  * Viewers distributed on `[0, 1]` with taste $\beta$. Two platforms $i \in \{1, 2\}$ located at $d_1, d_2 \in [0, 1]$.
  * Viewer utility with **quadratic** taste mismatch (which avoids the d'Aspremont et al. 1979 discontinuous market-tipping problem):
    $$U_i(\beta) = V - s_i - \delta a_i - t(\beta - d_i)^2$$
    where $s_i$ is subscription fee ($s_i = 0$ in Free TV), $\delta$ is ad annoyance, $a_i$ is ad volume, and $t$ is mismatch cost.
  * **Two-Stage Game (Platforms are strategic; viewers & advertisers respond):**
    * *Stage 1:* Platforms choose content locations $d_1, d_2$.
    * *Stage 2:* Platforms choose ad loads $a_1, a_2$ (and subscription fees $s_1, s_2$ if Pay TV).
  * **Audience Share:** Setting $U_1(\hat{\beta}) = U_2(\hat{\beta})$ pins down the indifferent viewer $\hat{\beta}$; with $d_1 < d_2$ and full coverage, Channel 1 gets $D_1 = \hat{\beta}$ and Channel 2 gets $D_2 = 1 - \hat{\beta}$.
* **Key Welfare Insight:** When viewers dislike ads, Free TV carries *higher* ad intensity and *more mainstream/similar* content than Pay TV (moving closer to the center steals eyeballs, traded off against softening ad competition by moving apart), whereas Pay TV differentiates more and moderates ads but excludes viewers via positive prices.

---

### Paper 4: Henriques (2021) — Airtime Caps & Endogenous Ad Quality
* **Citation:** Henriques, D. (2021). *"Effects of TV airtime regulation on advertising quality and welfare."* *Information Economics and Policy*, 55, 100897. (Elsevier, Q1).
* **Core Setup & Insight:** Makes **advertising quality** endogenous (entertaining/informative ads soften viewer ad disutility and reduce tune-out, at higher production cost to advertisers). Shows that a strict volume cap on TV ad minutes reduces broadcaster and advertiser profits and can *reduce* average ad quality—so a volume-only ad cap can backfire and lower viewer and total social welfare.

---

### Paper 5: Rothbauer & Sieg (2013) — Public Service Broadcasting & Rational Ignorance
* **Citation:** Rothbauer, J., & Sieg, G. (2013). *"Public Service Broadcasting of Sport, Shows, and News to Mitigate Rational Ignorance."* *Journal of Media Economics*, 26(1), 21–40. (Companion 2011 MPRA WP 33779: *"Welfare effects of public service broadcasting in a free-to-air TV market"*).
* **Core Setup & Insight:** Adds **positive civic externalities** from news consumption (better-informed voters control politicians) alongside Anthony Downs's **rational ignorance** (citizens under-consume pure news privately). Explains why a welfare-maximizing Public Service Broadcaster bundles **sports and entertainment shows** with **serious news** as a "Trojan horse" when marginal returns to information diminish sharply, weighing civic gains against public funding costs and lost private ad-market rents.

---

## 2. Empirical & Policy Benchmarks (For Calibration & Extensions)

* **Wilbur, K. C. (2008).** *"A Two-Sided, Empirical Model of Television Advertising and Viewing Markets."* *Marketing Science*, 27(3), 356–378.
  * Structural estimation of viewer ad-aversion and advertiser demand; counterfactual shows ad-avoidance tech causes networks to *raise* equilibrium ad loads on remaining viewers.
* **Goettler, R. L., & Shachar, R. (2001).** *"Spatial Competition in the Network Television Industry."* *RAND Journal of Economics*, 32(4), 704–736.
  * Empirical spatial-competition model on TV viewing panels; shows networks rely on scheduling rules of thumb that depart slightly from full Nash equilibrium.
* **Crawford, G. S., & Yurukoglu, A. (2012).** *"The Welfare Effects of Bundling in Multichannel Television Markets."* *American Economic Review*, 102(2), 643–685.
  * Benchmark structural Pay-TV bundling and wholesale bargaining model.
* **Poort, J., & Baarsma, B. (2016).** *"Measuring the Welfare Effects of Public Television."* *Journal of Media Economics*, 29(1), 2–17.
  * Combines Dutch viewing data with appreciation ratings and a 2.5%-of-net-income (€0.30/viewer-hour) benchmark + externality multipliers.
* **Nakamura, L., Samuels, J., & Soloveichik, R. (2016).** *"Valuing ‘Free’ Media in GDP: An Experimental Approach."* BEA WP 2016-3 / Philly Fed WP 15-25.
  * Production-cost / barter national-accounting approach (contrasted with consumer-surplus approaches like Brynjolfsson, Oh, & Varian).
* **Delaney, L., & O'Toole, F. (2004)** (*Economic and Social Review*), **Papandrea, F. (1999)** (*Journal of Cultural Economics*), and **Evens, Iosifidis, & Smith (2013)** (*Palgrave Macmillan* — sports rights & anti-siphoning laws).
