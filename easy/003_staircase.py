"""
Problem: Staircase
Source: HackerRank
Difficulty: Easy
Date: 2026-01-13

Description:
Write a program that prints a right-aligned staircase of size n using # symbols and spaces.
The staircase has both base and height equal to n.
The last line is not preceded by any spaces. All lines are right-aligned.

Examples:
n = 4
   #
  ##
 ###
####

n = 6
     #
    ##
   ###
  ####
 #####
######

Constraints:
- 0 < n <= 100
"""

def staircase(n):
    """
    Print a right-aligned staircase of size n.

    Args:
        n: an integer representing the size of the staircase

    Returns:
        None (prints the staircase)
    """
    pass

# Test cases
if __name__ == '__main__':
    import io
    from contextlib import redirect_stdout

    def capture(n):
        buf = io.StringIO()
        with redirect_stdout(buf):
            staircase(n)
        return buf.getvalue()

    # Test case 1
    output = capture(4)
    print(f"Test 1 (n=4):\n{output}", end='')
    assert output == "   #\n  ##\n ###\n####\n", f"Got: {output!r}"

    # Test case 2
    output = capture(6)
    print(f"Test 2 (n=6):\n{output}", end='')
    assert output == "     #\n    ##\n   ###\n  ####\n #####\n######\n", f"Got: {output!r}"

    # Test case 3: smallest staircase
    output = capture(1)
    print(f"Test 3 (n=1):\n{output}", end='')
    assert output == "#\n", f"Got: {output!r}"

    print("All tests passed!")
