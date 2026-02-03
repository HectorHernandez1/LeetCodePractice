# LeetCode Practice

Daily coding practice - One problem per day!

## Setup

### Python Environment
```bash
# Create the environment
conda env create -f environment.yml

# Activate the environment
conda activate leetcode
```

### Update Environment (if needed)
```bash
conda env update -f environment.yml --prune
```

### Running TypeScript Solutions
TypeScript solutions can be run using Bun:
```bash
# Run a specific TypeScript problem
bun easy/015_merge_sorted_array.ts
bun easy/020_best_time_to_buy_and_sell_stock.ts
```

## Progress

**Total Problems Solved:** 16
**TypeScript Versions:** 2 (in progress)

### Algorithm Problems
- Easy: 12
- Medium: 1
- Hard: 0 (1 added to solve)

**In Progress:** 1 (Medium - Add Two Numbers)

### Multi-Language Support
- Python: All problems
- TypeScript: Select problems (015 Merge Sorted Array, 020 Best Time to Buy and Sell Stock)

### Data Science Problems
- Completed: 2/7

## Problems Log

| # | Date | Problem | Difficulty | Source | Notes |
|---|------|---------|------------|--------|-------|
| 1 | 2026-01-09 | Diagonal Difference | Easy | HackerRank | Calculate absolute difference between diagonal sums of a square matrix |
| 2 | 2026-01-10 | Plus Minus | Easy | HackerRank | Calculate ratios of positive, negative, and zero elements |
| 3 | 2026-01-11 | Staircase | Easy | HackerRank | Print a right-aligned staircase pattern using # symbols |
| 4 | 2026-01-13 | Mini-Max Sum | Easy | HackerRank | Find min and max sums of 4 out of 5 integers |
| 5 | 2026-01-14 | Time Conversion | Easy | HackerRank | Convert 12-hour AM/PM format to 24-hour military time |
| 6 | 2026-01-16 | Insert Node at Tail | Easy | HackerRank | Insert a new node at the tail of a linked list |
| 7 | 2026-01-16 | Reverse Linked List | Easy | HackerRank/LeetCode #206 | Reverse a linked list using recursion or iteration |
| 8 | 2026-01-19 | Insert Node at Head | Easy | HackerRank | Insert a new node at the head of a linked list |
| 9 | 2026-01-19 | Sum to N | Medium | Classic | Find all combinations that sum to target using backtracking |
| 10 | 2026-01-21 | Grading Students | Easy | HackerRank | Round grades to nearest 5 based on rounding rules |
| 11 | 2026-01-23 | Two Sum | Easy | LeetCode #1 | Find two numbers that add up to target using nested loops |
| 12 | 2026-01-20 | Add Two Numbers (In Progress) | Medium | LeetCode #2 | Add two numbers represented as linked lists in reverse order |
| 13 | 2026-01-27 | Valid Parentheses | Easy | LeetCode #20 | Check if brackets are balanced using stack |
| 14 | 2026-01-29 | Valid Palindrome | Easy | LeetCode #125 | Check if string is palindrome using two-pointer technique |
| 15 | 2026-02-02 | Merge Sorted Array | Easy | LeetCode #88 | Merge two sorted arrays in-place using backward two-pointer technique |

## Study Plan

Currently focusing on: **Easy Problems**

## Additional Practice

### Data Engineering & Data Science Problems
A collection of 7 practical data problems focused on real-world data manipulation tasks:
- Data cleaning & aggregation (001) ✓
- Grouping & aggregation (002) ✓
- Time series analysis (003)
- Moving averages (004)
- Data deduplication (005)
- Pivot table implementation (006)
- ETL pipelines (007)

**Progress:** 2/7 completed

Each problem has its own file with tests. See: `datascience/` folder or `datascience/README.md`

## Notes & Tips

- Start with easy problems to build consistency
- Focus on understanding the problem before coding
- Write test cases first
- Document time and space complexity
- Review and optimize after solving
