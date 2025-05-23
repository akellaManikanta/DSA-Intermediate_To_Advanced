"""
Problem Description
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

Problem Constraints
1 <= A.size() <= 10^3
1 <= A[i].size() <= 10^3
1 <= A[i][j] <= 10^3

Input Format
First argument is a 2D array of integers.(2D matrix).

Output Format
Return an array containing column-wise sums of original matrix.

Example Input
Input 1:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Example Output
Output 1:
{15,10,13,16}

Example Explanation
Explanation 1
Column 1 = 1+5+9 = 15
Column 2 = 2+6+2 = 10
Column 3 = 3+7+3 = 13
Column 4 = 4+8+4 = 16
"""
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def bruteforce(self, A):
        pass

    def optmised(self, A):
        result = []
        for column in range(len(A[0])):
            sum = 0
            for row in range(len(A)):
                sum += A[row][column]
            result.append(sum)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.optmised([[1,2,3,4],
                 [5,6,7,8],
                 [9,2,3,4]]))