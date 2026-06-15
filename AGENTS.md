# AGENTS.md — LeetCode Practice

## Project overview
- Personal coding practice repo: one problem per day from LeetCode, HackerRank, and classics.
- Three difficulty tiers: `easy/`, `medium/`, `hard/`
- `datascience/` — separate data engineering problems (pandas/numpy or pure Python)
- Primary language: Python. Also TypeScript, JavaScript, C# for select problems.

## Quick commands

```bash
# Python solutions (the majority)
python easy/XXX_problem.py

# TypeScript solutions (uses Bun, not ts-node)
bun easy/015_merge_sorted_array.ts

# JavaScript solutions
node medium/XXX_problem.js

# C# solutions
dotnet-script medium/XXX_problem.cs
```

- **Condaless setup**: `pip install -r requirements.txt` (just pytest) is enough unless numpy/pandas are needed for `datascience/`.
- **Conda setup**: `conda env create -f environment.yml && conda activate leetcode`

## Conventions

### File naming
- Format: `XXX_problem_name.ext` — zero-padded 3-digit number, snake_case.
- Each difficulty folder has its own sequential numbering.
- Multi-language variants share the same number prefix (e.g., `004_count_primes_in_range.py`, `.js`, `.cs`).

### Solution structure
- Every file is self-contained: problem description, `Solution` class, inline test runner.
- **No external test framework is used** — tests run by executing the file directly (`python <file>`).
- Use `template.py` as the blueprint for new problems.

### After solving a problem
- **Must** update `README.md`:
  1. Increment the total problems-solved count.
  2. Add a row to the Problems Log table (date, problem, difficulty, source, notes).
  3. Update difficulty breakdown counts.
- Optionally update `TODO.md` to mark problems complete.

## Important notes
- No CI, no linting, no typechecking configured for this repo.
- The `.claude.md` file contains detailed coding conventions, the "coding teacher" persona, and commit-message rules (no `Co-Authored-By` attributions). Consult it for style guidance.
- Git: keep commits focused on single problems. Format: `Add [Problem Name] problem for day N`.
