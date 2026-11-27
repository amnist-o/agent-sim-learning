# Project Status — Agent-Based Simulation Learning Lab (`agent-sim-learning`)

## 2026-11-27 — Lesson 00 Completed & Lesson 01 Crafted

### What we did & decided
- **Completed Lesson 00 (`lessons/00_python_warmup/work.py`):**
  - Debugged Python data structures (distinguishing `numpy` arrays, dictionaries, and lists of dictionaries), `f-string` number formatting (`4.1f`, `7.4f`), and a subtle variable-scope bug (`a_0`/`a_1` leaking into `evaluate_market`).
  - Verified all baseline numbers (`share_0 = 0.7502`, `share_1 = 0.2498`, `profit_0 = 1.3006`, `profit_1 = 0.2992`) and the Task 3 sweep: Channel 1's profit peaks at `a_1 = 5.0` (`0.7488`), while Total Social Welfare peaks in the interior at `a_1 = 4.5` (`8.3494`) due to the trade-off between taste mismatch at very low `a_1` and viewer ad annoyance at higher `a_1`.
  - **Modeling decision (tie-breaking):** A. deliberately chose `u_i > u_off` (indifferent viewers at `u = 0` leave the TV off) as a more natural economic assumption; confirmed mutually exclusive and exhaustive choice rules.
- **Crafted Lesson 01 (`lessons/01_mesa_baseline/`):**
  - Created `README.md` and starter `work.py` extending Lesson 00 into a dynamic **Mesa 3** model where both broadcasters adjust ad loads via myopic local search (`step_size = 0.5`) and converge to the Peitz & Valletti (2008) Stage-2 Nash Equilibrium (`a_0 = a_1 = 4.0`, `welfare = 8.5165`).
  - Added an **ad-cap policy experiment** (`a_max` in `[2.0, 3.0, 4.0, 6.0]`) to surface the profitability/bankruptcy trade-off at strict caps (`a_max = 2.0` yields negative broadcaster profits despite higher static welfare).
- **Environment note on this machine:** Root `.venv/` is not yet present on this Windows machine (only global Python 3.14 with `numpy`, no `mesa`). Before running Lesson 01 here, create/activate `.venv` and install `mesa`, `numpy`, `pandas`, `matplotlib`.

### Current status
- **State now:** Lesson 00 is complete and verified; Lesson 01 (`lessons/01_mesa_baseline/README.md` and starter `work.py`) is ready.
- **Next action:** Install `mesa` (and `pandas`) in `.venv` on this machine if needed, then A. writes `lessons/01_mesa_baseline/work.py` and submits it for trainer code review.
- **Waiting on / open questions:** Waiting on A.'s first draft of `lessons/01_mesa_baseline/work.py`.

---

## 2026-11-25 — Project Setup & Lesson 00 Ready

### What we did & decided
- **Goal:** Build a hands-on learning lab for Agent-Based Computational Economics (ACE) grounded in the theoretical and empirical Free-TV social welfare papers reviewed earlier (archived locally in `docs/literature_reference.md`).
- **Tool choice (`Python 3.15` + `Mesa 3`):** Chosen over NetLogo and plain R because Mesa is the active flagship standard for ABM, combines clean agent/market structure with interactive sliders and reproducible Monte Carlo sweeps, and transfers directly to future research.
- **Training mode:** A. writes the full code for each lesson after studying syntax building-block examples; Gemini acts strictly as a trainer/reviewer—critiquing correctness, clarity, vectorization/efficiency, and economic edge cases until each lesson's code is clean and solid.
- **Revisitable folder layout:** Each lesson lives in its own subfolder under `lessons/` (`00_python_warmup/`, `01_mesa_baseline/`, etc.) with a permanent `README.md` (problem, examples, check-numbers) and `work.py` (so A. can revisit or redo any lesson in a new file like `redo_1.py` without losing earlier work).

### Current status
- **State now:** Project structure, `.gitignore`, `docs/literature_reference.md`, `docs/r_to_python_cheatsheet.md`, and `lessons/00_python_warmup/` are set up; `.venv/` verified with `mesa 3.5.3`, `numpy 2.5.5`, `pandas 3.1.1`, and `matplotlib 3.11.2`.
- **Next action:** A. writes `lessons/00_python_warmup/work.py` and submits it for trainer code review.
- **Waiting on / open questions:** Waiting on A.'s first draft of `lessons/00_python_warmup/work.py`.
