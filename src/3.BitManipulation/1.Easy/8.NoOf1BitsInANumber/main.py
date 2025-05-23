"""
Problem Description
Write a function that takes an integer and returns the number of 1 bits present in its binary representation.



Problem Constraints
1 <= A <= 10^9

Input Format
First and only argument contains integer A

Output Format
Return an integer

Example Input
Input 1:
11

Input 2:
6

Example Output
Output 1:
3

Output 2:
2

Example Explanation
Explaination 1:
11 is represented as 1011 in binary.

Explaination 2:
6 is represented as 110 in binary.
"""
class Solution:
    def num_set_bits(self, A):
        counter = 0
        for i in range(32):
            if (A >> i) & 1 == 1:
                counter += 1
        return counter


if __name__ == "__main__":
    sol = Solution()
    print(sol.num_set_bits(11))