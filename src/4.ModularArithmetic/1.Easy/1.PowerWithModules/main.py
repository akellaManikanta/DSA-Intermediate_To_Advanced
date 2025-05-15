"""
Problem Description
You are given A, B and C .
Calculate the value of (A ^ B) % C

Problem Constraints
1 <= A <= 10^9
0 <= B <= 10^5
1 <= C <= 10^9

Input Format
Given three integers A, B and C.

Output Format
Return an integer.

Example Input
Input 1:
A = 2
B = 3
C = 3

Input 2:
A = 5
B = 2
C = 4

Example Output
Output 1:
2

Output 2:
1

Example Explanation
For Input 1:
(2 ^ 3) % 3 = 8 % 3 = 2

For Input 2:
(5 ^ 2) % 4 = 25 % 4 = 1
"""


class Solution:
    def powers_with_modules(self, A: int, B: int, C: int):
        ans = 1
        for i in range(1, B+1, 1):
            ans = ((ans % C) * (A % C)) % C
        return ans


if __name__ == "__main__":
    A = 5
    B = 2
    C = 4
    sol = Solution()
    print(sol.powers_with_modules(A, B, C))
