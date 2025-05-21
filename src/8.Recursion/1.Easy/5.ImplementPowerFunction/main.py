"""
Problem Description

Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.



Problem Constraints

-10^9 <= A <= 10^9
0 <= B <= 10^9
1 <= C <= 10^9

Input Format
Given three integers A, B, C.

Output Format
Return an integer.

Example Input
Input 1:
A = 2
B = 3
C = 3

Input 2:
A = 3
B = 3
C = 1

Example Output
Output 1:
2
Output 2:
0
"""
class Solution:
    def power(self, A, B, C):
        if B == 0:
            if A == 0:
                return 0
            return 1
        elif B == 1:
            return A % C
        else:
            exponent = self.power(A, B // 2, C)
            if B % 2 == 0:
                return ((exponent % C) * (exponent % C)) % C
            else:
                return ((A % C) * (exponent % C) * (exponent % C)) % C

if __name__ == "__main__":
    sol = Solution()
    sol.power(-1, 1, 20)
    sol.power(0, 0, 20)