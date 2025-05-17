"""
Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109

Input Format
The first argument is an array of integers.

Output Format
Return a string representing the largest number.

Example Input
Input 1:
 A = [3, 30, 34, 5, 9]

Input 2:
 A = [2, 3, 9, 0]

Example Output
Output 1:
 "9534330"

Output 2:
 "9320"
"""
from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @return a strings
    def largestNumber(self, A):
        A = [str(i) for i in A]
        A.sort(key=cmp_to_key(Solution.compare_vals))
        result = "".join(A)
        return result.lstrip("0") or "0"

    @staticmethod
    def compare_vals(x, y): # Read https://docs.python.org/3.12/howto/sorting.html#comparison-functions to know more.
        if int(x+y) > int(y+x):
            return -1
        elif int(x+y) < int(y+x):
            return 1
        else:
            return 0