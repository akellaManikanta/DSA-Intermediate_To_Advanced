"""
Problem Description
You are given a number A. You are also given a base B. A is a number on base B.
You are required to convert the number A into its corresponding value in decimal number system.

Problem Constraints
0 <= A <= 10^9
2 <= B <= 9

Input Format
First argument A is an integer.
Second argument B is an integer.

Output Format
Return an integer.

Example Input
Input 1:
A = 1010
B = 2

Input 2:
A = 22
B = 3

Example Output
Output 1:
10

Output 2:
8
"""

class Solution:
    def convert(self, number, base):
        converted_number = 0
        power = 1
        while number > 0:
            digit = number % 10
            converted_number += digit * power
            power *= base
            number = number // 10
        return converted_number


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert(1010, 2))