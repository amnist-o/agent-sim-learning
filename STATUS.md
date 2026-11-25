# Project Status — Agent-Based Simulation Learning Lab (`agent-sim-learning`)

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
