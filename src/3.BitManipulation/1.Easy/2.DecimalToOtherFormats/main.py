"""
Problem Description
Given a decimal number A and a base B, convert it into its equivalent number in base B.

Problem Constraints
0 <= A <= 512
2 <= B <= 10

Input Format
The first argument will be decimal number A.
The second argument will be base B.

Output Format
Return the conversion of A in base B.

Example Input
Input 1:
A = 4
B = 3

Input 2:
A = 4
B = 2

Example Output
Output 1:
11

Output 2:
100

Example Explanation
Explanation 1:
Decimal number 4 in base 3 is 11.

Explanation 2:
Decimal number 4 in base 2 is 100.
"""
class Solution:
    def convert_from_decimal(self, number, base):
        converted = []
        if number == 0:
            return 0
        while number > 0:
            remainder = number % base
            converted.append(remainder)
            number = number // base
        return int("".join([str(i) for i in converted[::-1]]))


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert_from_decimal(4, 2))