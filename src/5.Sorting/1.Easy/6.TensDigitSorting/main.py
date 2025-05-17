"""
Problem Description

Given an array A of N integers. Sort the array in increasing order of the value at the tens place digit of every number.
    If a number has no tens digit, we can assume value to be 0.
    If 2 numbers have same tens digit, in that case number with max value will come first
    Solution should be based on comparator.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9

Input Format
First argument A is an array of integers.

Output Format
Return the array after sorting

Example Input
Input 1:
A = [15, 11, 7, 19]

Input 2:
A = [2, 24, 22, 19]

Example Output
Output 1:
[7, 19, 15, 11]

Output 2:
[2, 19, 24, 22]

Example Explanation
For Input 1:
The sorted order is [7, 19, 15, 11]. The tens digit of 7 is 0,
and that of 19, 15 and 11 is 1.

For Input 2:
The sorted order is [2, 19, 24, 22]. The tens digit of 2 is 0,
that of 19 is 1 and that of 22 and 24 is 2.
"""
from functools import cmp_to_key


class Solution():
    def bruteforce(self, A):
        len_array = len(A)
        for i in range(len_array):
            for j in range(i+1, len_array):
                if (A[i] // 10) % 10 > (A[j]  // 10) % 10:
                    A[i], A[j] = A[j], A[i]
        return A

    def optimised(self, A):
        return sorted(A, key=cmp_to_key(self.sort_on_tens_digit))

    def sort_on_tens_digit(self, x, y):
        tx = (x // 10) % 10
        ty = (y // 10) % 10

        if tx != ty:
            return tx - ty # returns + ve or - ve value
        else:
            return y - x # on tie it returns the + ve or -ve value

if __name__ == "__main__":
    A = [7, 19, 15, 11]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))