"""
Problem Description
Given a number in the form of an array A of size N. Each of the digits of the number is represented by A[i]. Check if the number is divisible by 3.

Problem Constraints
1 <= N <= 10^5
0 <= A[i] <= 9
A[1] ≠ 0

Input Format
Given an integer array representing the number

Output Format
Return 1 if the number is divisible by 3 and return 0 otherwise.

Example Input
Input 1:
A = [1, 2, 3]

Input 2:
A = [1, 0, 0, 1, 2]

Example Output
Output 1:
1

Output 2:
0
"""
class Solution:
    def divisibility_by_3(self, A:list[int]):
        sum = 0
        for i in A:
            sum = sum + i
        if sum % 3 == 0:
            return 1
        else:
            return 0