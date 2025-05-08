"""
Problem Description

You are given an integer A. You have to tell whether it is a perfect number or not.
Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
A proper divisor of a natural number is the divisor that is strictly less than the number.

Problem Constraints

1 <= A <= 10**6

Input Format
First and only argument contains a single positive integer A.

Output Format
Return 1 if A is a perfect number and 0 otherwise.

Example Input
Input 1:
A = 4

Input 2:
A = 6

Example Output
Output 1:
0

Output 2:
1
"""

class Solution:
    def bruteforce(self, A): # TC: O(N), SC:O(1)
        sum = 0
        for i in range(1, A):
            if A % i == 0:
                sum += i
        return 1 if sum == A else 0

    def optimised(self, A): # TC: O(SQRT(N)), SC:O(1)
        sum = 1
        i = 2
        while i * i <= A:
            if A // i == i:
                sum += i
            elif A % i == 0:
                sum += i
                sum += A // i
            i += 1
        return 1 if sum == A else 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce(6))
    print(sol.bruteforce(4))
    print(sol.optimised(6))
    print(sol.optimised(4))


