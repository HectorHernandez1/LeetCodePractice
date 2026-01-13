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
    # Write your code here
    pass


# Test cases
if __name__ == '__main__':
    # Test case 1
    print("Test 1 (n=4):")
    staircase(4)
    # Expected output:
    #    #
    #   ##
    #  ###
    # ####
    print()

    # Test case 2
    print("Test 2 (n=6):")
    staircase(6)
    # Expected output:
    #      #
    #     ##
    #    ###
    #   ####
    #  #####
    # ######
    print()

    # Test case 3
    print("Test 3 (n=1):")
    staircase(1)
    # Expected output:
    # #
