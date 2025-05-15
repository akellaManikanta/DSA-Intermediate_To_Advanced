"""
Problem Description
You are given two integers A and B.
Set the A-th bit and B-th bit in 0, and return output in decimal Number System.

Note:
The bit positions are 0-indexed, which means that the least significant bit (LSB) has index 0.

Problem Constraints
0 <= A <= 30
0 <= B <= 30

Input Format
First argument A is an integer.
Second argument B is an integer.

Output Format
Return an integer.

Example Input
Input 1:
A = 3
B = 5

Input 2:

A = 4
B = 4

Example Output
Output 1:
40

Output 2:
16
"""
class Solution:
    def set_given_bits(self, A, B):
        number = [0]*32
        number[31-A] = 1
        number[31-B] = 1
        power = 1
        counter = 0
        result = 0
        while counter <= max(A, B):
            result += number[31 - counter] * power
            power *= 2
            counter += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.set_given_bits(4,4))

