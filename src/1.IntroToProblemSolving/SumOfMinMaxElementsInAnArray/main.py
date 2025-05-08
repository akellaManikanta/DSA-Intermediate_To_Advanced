"""
Problem Description
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
First argument A is an integer array.

Output Format
Return the sum of maximum and minimum element of the array

Example Input
Input 1:
A = [-2, 1, -4, 5, 3]
Input 2:
A = [1, 3, 4, 1]

Example Output
Output 1:
1

Output 2:
5
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def bruteforce_and_optimised(self, A):
        min_element = A[0]
        max_element = A[0]
        for i in range(1, len(A)):
            if A[i] < min_element:
                min_element = A[i]
            if A[i] > max_element:
                max_element = A[i]
        return min_element + max_element


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce_and_optimised([1,2,3,4]))
