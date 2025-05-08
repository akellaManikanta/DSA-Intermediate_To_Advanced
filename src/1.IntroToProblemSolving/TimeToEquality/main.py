"""
Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Problem Constraints
1 <= N <= 10^6
1 <= A[i] <= 10^3

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the minimum time to make all elements equal.

Example Input
A = [2, 4, 1, 3, 2]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def bruteforce_an_optimised(self, A):
        largest_element = A[0]
        for i in range(1, len(A)):
            largest_element = max(largest_element, A[i])
        time = 0
        for item in A:
            time += largest_element - item
        return time


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce_an_optimised([2, 4, 1, 3, 2]))
