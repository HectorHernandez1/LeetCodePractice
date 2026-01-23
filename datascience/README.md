# Data Engineering & Data Science Problems

This folder contains practical data manipulation problems common in data engineering and data science interviews.

## Problems Overview

| # | Problem | Difficulty | Focus Area |
|---|---------|------------|------------|
| 1 | Data Cleaning & Aggregation | Easy-Medium | Data cleaning, grouping, averaging |
| 2 | Grouping & Aggregation | Medium | Aggregation, sorting, top-N queries |
| 3 | Time Series Analysis | Medium | Time series, consecutive patterns |
| 4 | Moving Average | Medium | Sliding window, time series |
| 5 | Data Deduplication | Medium | Deduplication, timestamp handling |
| 6 | Pivot Table Implementation | Medium-Hard | Multi-dimensional aggregation |
| 7 | ETL Pipeline | Hard | Data pipelines, transformations |

## How to Use

Each problem is in its own file with:
- Problem description and examples
- Function stub to implement
- Test cases

Run individual problem files:
```bash
python datascience/001_data_cleaning_aggregation.py
python datascience/002_grouping_aggregation.py
# ... and so on
```

## Approach

These problems can be solved in two ways:

1. **Pure Python** - Using built-in data structures (lists, dicts, sets)
   - Good for understanding core concepts
   - Common in technical interviews

2. **Pandas/NumPy** - Using data science libraries
   - More realistic for real-world data engineering
   - Faster for large datasets
   - Good practice for data science roles

## Dependencies

Install required packages:
```bash
conda activate leetcode
conda install numpy pandas
```

Or update from environment.yml:
```bash
conda env update -f environment.yml --prune
```

## Tips

- Start with pure Python solutions to understand the logic
- Then optimize or rewrite using pandas if appropriate
- Focus on data manipulation patterns: grouping, aggregation, filtering, transformation
- These problems mimic real-world data tasks you'll encounter in data engineering/science roles
