"""
Problem Description
Given an array A of N integers. Construct prefix sum of the array in the given array itself.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^3

Input Format
Only argument A is an array of integers.

Output Format
Return an array of integers denoting the prefix sum of the given array.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]

Input 2:
A = [4, 3, 2]

Example Output
Output 1:
[1, 3, 6, 10, 15]

Output 2:
[4, 7, 9]
"""

class Solution:
    def optimised(self, A):
        prefix_sum = [0]*len(A)
        for i in range(len(A)):
            if i == 0:
                prefix_sum[0] = A[0]
            else:
                prefix_sum[i] = A[i] + prefix_sum[i-1]
        return prefix_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.optimised([1, 2, 3, 4, 5]))