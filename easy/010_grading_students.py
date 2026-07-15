#!/bin/python3
"""
Problem: Grading Students
Source: HackerRank
Difficulty: Easy
Date: 2026-01-19

Description:
HackerLand University has the following grading policy:

- Every student receives a grade in the inclusive range from 0 to 100.
- Any grade less than 38 is a failing grade.

Sam is a professor at the university and likes to round each student's grade
according to these rules:

- If the difference between the grade and the next multiple of 5 is less than 3,
  round grade up to the next multiple of 5.
- If the value of grade is less than 38, no rounding occurs as the result will
  still be a failing grade.

Examples:
- grade = 84 -> round to 85 (85 - 84 is less than 3)
- grade = 29 -> do not round (result is less than 38)
- grade = 57 -> do not round (60 - 57 is 3 or higher)

Function Description:
Complete the gradingStudents function with the following parameter(s):
    grades: the grades before rounding

Returns:
    list[int]: the grades after rounding

Input Format:
The first line contains a single integer, n, the number of students.
Each line i of the n subsequent lines contains a single integer, grades[i].

Constraints:
- 1 <= n <= 60
- 0 <= grades[i] <= 100

Sample Input:
4
73
67
38
33

Sample Output:
75
67
40
33

Explanation:
- Student 1 received a 73, and the next multiple of 5 from 73 is 75.
  Since 75 - 73 < 3, the student's grade is rounded to 75.
- Student 2 received a 67, and the next multiple of 5 from 67 is 70.
  Since 70 - 67 = 3, the grade will not be modified and the final grade is 67.
- Student 3 received a 38, and the next multiple of 5 from 38 is 40.
  Since 40 - 38 < 3, the student's grade will be rounded to 40.
- Student 4 received a grade below 38, so the grade will not be modified
  and the final grade is 33.
"""

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    """
    Round student grades according to the university policy.

    Args:
        grades: list of integers representing student grades

    Returns:
        list[int]: the grades after applying rounding rules
    """
    pass


# Test cases
if __name__ == '__main__':
    # Test case 1: Sample input
    grades = [73, 67, 38, 33]
    result = gradingStudents(grades)
    print(f"Test 1: {grades} -> {result} (expected [75, 67, 40, 33])")
    assert result == [75, 67, 40, 33], f"Got: {result}"

    # Test case 2
    grades = [84, 29, 57]
    result = gradingStudents(grades)
    print(f"Test 2: {grades} -> {result} (expected [85, 29, 57])")
    assert result == [85, 29, 57], f"Got: {result}"

    # Test case 3: Boundary cases (below 38, exact multiples, 0 and 100)
    grades = [37, 38, 40, 100, 0]
    result = gradingStudents(grades)
    print(f"Test 3: {grades} -> {result} (expected [37, 40, 40, 100, 0])")
    assert result == [37, 40, 40, 100, 0], f"Got: {result}"

    # Test case 4: Just below/above rounding threshold
    grades = [83, 84, 85, 86, 87]
    result = gradingStudents(grades)
    print(f"Test 4: {grades} -> {result} (expected [85, 85, 85, 86, 87])")
    assert result == [85, 85, 85, 86, 87], f"Got: {result}"

    print("All tests passed!")
