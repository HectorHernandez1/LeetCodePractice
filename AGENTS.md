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

## Working in this repo
- **At the start of every session**, load the `engineer-mentor` skill (`.opencode/skills/engineer-mentor/SKILL.md`) and follow its persona/modes for all work.
- **Before writing a solution**, read `template.py` and one existing sibling file in the target difficulty folder to match the exact style (docstring header, `Solution` class, inline test block).
- **Every solution is self-contained** — no shared modules, no external test framework. Tests live in the file's `if __name__ == "__main__"` (Python) / `runTests()` (TypeScript) block and use `assert`.
- **Always document time and space complexity** in the method docstring.
- **Prefer clarity over cleverness** — don't over-engineer. Optimize only after a correct solution exists.
- **When unsure** about scope (new language, large refactor, changing conventions), ask before proceeding.

## Verification (required before considering work done)
- Run the file directly and confirm it prints `All tests passed!` (or equivalent) with zero errors:
  - `python easy/XXX_problem.py`
  - `bun easy/XXX_problem.ts`
  - `node medium/XXX_problem.js`
  - `dotnet-script medium/XXX_problem.cs`
- Cover edge cases in tests: empty input, single element, large input, negative numbers (where relevant).
- Do not mark a problem complete unless the file runs clean and `README.md` counts are updated.

## Important notes
- No CI, no linting, no typechecking configured for this repo.
- The `.claude.md` file contains the "coding teacher" persona and detailed coding conventions. Consult it for style guidance; this `AGENTS.md` is the cross-tool source of truth for commands, structure, and workflow.
- Commit messages must **not** include `Co-Authored-By` attributions.
- Git: keep commits focused on single problems. Format: `Add [Problem Name] problem for day N`.
