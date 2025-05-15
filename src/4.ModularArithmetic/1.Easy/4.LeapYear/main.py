"""
Problem Description
Given an integer A representing a year, Return 1 if it is a leap year else, return 0.
A year is a leap year if the following conditions are satisfied:
    The year is multiple of 400.
    or the year is multiple of 4 and not multiple of 100.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A

Output Format
Return 1 if it is a leap year else return 0

Example Input
Input 1
 A = 2020

Input 2:
 A = 1999

Example Output
Output 1
 1

Output 2:
 0
"""
class Solution:
    # @param A : integer
    # @return an integer
    def leap_year(self, year):
        if year % 400 == 0:
            return 1
        elif year % 4 == 0 and year % 100 != 0:
            return 1
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.leap_year(1999))