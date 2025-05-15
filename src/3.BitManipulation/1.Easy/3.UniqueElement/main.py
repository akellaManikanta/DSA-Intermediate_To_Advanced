"""
Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Problem Constraints
    1 <= |A| <= 2000000
    0 <= A[i] <= INTMAX

Input Format
The first and only argument of input contains an integer array A.

Output Format
Return a single integer denoting the single element.



Example Input
Input 1:
 A = [1, 2, 2, 3, 1]

Input 2:
 A = [1, 2, 2]
"""
class Solution:
    def bruteforce(self, A):
        count = 0
        arr_length = len(A)
        for i in range(arr_length):
            count = 0
            for j in range(arr_length):

                if A[i] == A[j]:
                    count += 1
            if count == 1:
                return A[i]
        return None

    def optimised(self, A):
        element = 0
        for i in A:
            element ^= i
        return element


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([1, 2, 2, 3, 1]))
    print(sol.optimised([1, 2, 2, 3, 1]))
