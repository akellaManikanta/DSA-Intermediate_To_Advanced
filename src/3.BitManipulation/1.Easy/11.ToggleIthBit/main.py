"""
Problem Description
You are given two integers A and B.
    If B-th bit in A is set, make it unset
    If B-th bit in A is unset, make it set

Return the updated A value

Problem Constraints
1 <= A <= 109
0 <= B <= 30

Input Format
First argument A is an integer.
Second argument B is an integer.


Output Format
Return an integer.

Example Input
Input 1:
A = 4
B = 1

Input 2:

A = 5
B = 2

Example Output
Output 1:
6

Output 2:
1
"""

class Solution:
    def toggle_i_th_bit(self, A, B):
        return A ^ (1 << B)

if __name__ == "__main__":
    sol = Solution()
    print(sol.toggle_i_th_bit(4, 1))
