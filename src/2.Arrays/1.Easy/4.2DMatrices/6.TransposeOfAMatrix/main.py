"""
Problem Description
Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000

Input Format
First argument is a 2D matrix of integers.

Output Format
You have to return the Transpose of this 2D matrix.

Example Input
Input 1:
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

Input 2:
A = [[1, 2],[1, 2],[1, 2]]

Example Output
Output 1:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Output 2:
[[1, 1, 1], [2, 2, 2]]
"""
class Solution:
    def bruteforce(self, A):
        rows = len(A)
        cols = len(A[0])
        result = []
        for _ in range(cols):
            new_row = []
            for _ in range(rows):
                new_row.append(0)
            result.append(new_row)
        for i in range(rows):
            for j in range(cols):
                result[j][i] = A[i][j]
        return result


if __name__ == "__main__":
    A = [[24, 21, 33, 62, 81, 26, 45, 64, 43, 94],
         [63, 64, 6, 88, 58, 40, 44, 34, 42, 25],
         [39, 95, 63, 23, 74, 88, 86, 83, 7, 62],
         [81, 6, 96, 52, 18, 64, 92, 26, 17, 19],
         [84, 88, 86, 94, 16, 72, 50, 29, 45, 95],
         [30, 73, 66, 77, 25, 23, 26, 68, 52, 77]
         ]
    sol = Solution()
    print(sol.bruteforce(A))
