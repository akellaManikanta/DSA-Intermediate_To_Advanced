class Solution:
    # @param A : long
    # @return an integer
    def bruteforce(self, A):
        if A == 1:
            return 0
        elif A == 2:
            return 1
        for i in range(2, A):
            if A % i == 0:
                return 0
        return 1

    def optimised(self, A):
        if A <= 1:
            return 0
        if A == 2:
            return 1
        if A % 2 == 0:
            return 0
        i = 3
        while i * i <= A:
            if A % i == 0:
                return 0
            i += 2
        return 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce(97))
    print(sol.optimised(97))
