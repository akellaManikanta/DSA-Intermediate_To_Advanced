"""
Problem Description

Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Problem Constraints
2 <= N <= 10^5
-109 <= A[i] <= 10^9

Input Format
The first and only argument is an integer array A of size N.

Output Format
Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.

Example Input
Input 1:
 A = [3, 5, 1]
Input 2:
 A = [2, 4, 1]

Example Output
Output 1:
 1

Output 2:
 0

Example Explanation
Explanation 1:
 We can reorder the elements as [1, 3, 5] or [5, 3, 1] with differences 2 and -2 respectively, between each consecutive elements.

Explanation 2:
 There is no way to reorder the elements to obtain an arithmetic progression.
"""

class Solution():
    def bruteforce(self, A):
        len_arr = len(A)
        if len(A) == 2:
            return 1
        for i in range(len_arr):
            for j in range(i, len_arr):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        common_difference = A[1] - A[0]
        for i in range(2, len_arr):
            if A[i] - A[i-1] != common_difference:
                return -1
        return 1

    def optimised(self, A):
        len_arr = len(A)
        if len(A) == 2:
            return 1
        A.sort()
        common_difference = A[1] - A[0]
        for i in range(2, len_arr):
            if A[i] - A[i-1] != common_difference:
                return 0
        return 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([3,1,5]))
    print(sol.optimised([3,1,5]))