"""
Given a number A. Return square root of the number if it is perfect square otherwise return -1.

Note: A number is a perfect square if its square root is an integer.

Problem Constraints
1 <= A <= 108

Input Format
First and the only argument is an integer A.

Output Format
Return an integer which is the square root of A if A is perfect square otherwise return -1.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def bruteforce(self, A): # TC O(N) SC: O(1)
        for i in range(A):
            if i * i == A:
                return i
        return -1

    def optimised(self, A): # TC O(SQRT(N)) SC: O(1)
        i = 1
        while i * i < A:
            if i * i == A:
                return i
        return -1
