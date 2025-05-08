# Given any number A, Find number of factors:
# 1 <= A <= 10**9

class Solution:
    def bruteforce(self, A):
        count_of_factors = 0
        for i in range(1, A+1):
            if A%i == 0:
                count_of_factors += 1
        return count_of_factors

    def optimised(self, A):
        count_of_factors = 0
        i = 1
        while i * i <= A:
            if i == A// i:
                count_of_factors += 1
            elif A%i == 0:
                count_of_factors += 2
            i += 1
        return count_of_factors


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce(100))
    print(sol.optimised(100))
