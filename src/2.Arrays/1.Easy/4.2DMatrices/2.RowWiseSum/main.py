""""""
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def bruteforce(self, A):
        pass

    def optimised(self, A):
        result = []
        for i in range(len(A)):
            sum = 0
            for j in range(len(A[i])):
                sum += A[i][j]
            result.append(sum)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.optimised([[1,2,3,4],
                        [5,6,7,8],
                        [9,2,3,4]]))