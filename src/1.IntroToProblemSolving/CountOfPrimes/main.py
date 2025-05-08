"""
Problem Description
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.

Problem Constraints

0 <= n <= 10^3

Input Format
Single input parameter n in function.

Output Format
Return the count of prime numbers less than or equal to n.

Example Input
Input 1:
19

Input 2:
1

Example Output
Output 1:
8

Output 2:
0
"""
class Solution:
    def bruteforce(self, A):
        count = 0
        primes = []
        i = 1
        if A <= 1:
            return 0, []
        else:
            for i in range(2, A + 1):
                is_prime = True
                for j in range(2, i):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(i)
                    count += 1
        return count, primes

    def optimised(self, A): # TC: O(n log log n) SC: O(n)
        is_prime = [True] * (A + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(A ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, A + 1, i):
                    is_prime[j] = False

        primes = [i for i, val in enumerate(is_prime) if val]
        return len(primes), primes

if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce(19)) # [2, 3, 5, 7, 11, 13, 17, 19]
