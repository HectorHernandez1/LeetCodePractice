# AGENTS.md — LeetCode Practice

## Project overview
- Personal practice repo: one problem per day (LeetCode, HackerRank, classics).
- Folders: `easy/`, `medium/`, `hard/`, plus `datascience/` (pandas/numpy or pure-Python data problems).
- Languages: primarily Python; TypeScript, JavaScript, C# for select problems.

## Run a solution
```bash
python easy/XXX_problem.py           # Python
bun easy/015_merge_sorted_array.ts   # TypeScript — uses Bun, NOT ts-node/node
node medium/XXX_problem.js           # JavaScript
dotnet-script medium/XXX_problem.cs  # C#
```
- **No test framework is used, even though `pytest` is in `requirements.txt`.** Tests are inline `assert`s inside the file; a clean run prints `All tests passed!`. Do NOT create pytest files or shared modules.
- Setup: `pip install -r requirements.txt` is sufficient. Conda alternative: `conda env create -f environment.yml && conda activate leetcode` (needed only for numpy/pandas in `datascience/`).

## Conventions
- **Filename:** `XXX_problem_name.ext` — zero-padded 3-digit, snake_case. Numbering is independent per difficulty folder. Multi-language variants share the same number prefix (e.g. `004_count_primes_in_range.{py,js,cs}`).
- **Every file is self-contained:** header docstring (problem, source, difficulty, date, description, constraints) → `Solution` class → inline test block. Files may currently be blank stubs (`pass`) awaiting implementation — implement the method body and the test block.
- **Test block:** Python `if __name__ == "__main__"`; TypeScript `runTests()`. Use `assert`; print `All tests passed!` on success.
- Document time and space complexity in the method docstring.
- No CI, linting, or typechecking is configured.
- `template.py` is the blueprint. Read it plus one sibling in the target folder before writing anything new.

## After solving a problem
- Update `README.md`: increment total count, add a Problems Log row (date, problem, difficulty, source, notes), and update the difficulty breakdown.
- Optionally mark complete in `TODO.md`.

## Working in this repo
- Load the `engineer-mentor` skill at session start; follow its Build/Teach modes. This `AGENTS.md` is the source of truth; `.claude.md` holds the older "coding teacher" persona (consult for style only).
- In Teach mode (user asks for help/explanation), guide with hints — do not hand over finished solutions.

## Commits
- Focused on single problems: `Add [Problem Name] problem for day N`.
- Never include `Co-Authored-By` attributions.
