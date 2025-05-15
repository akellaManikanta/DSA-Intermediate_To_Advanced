"""
Problem Description
You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.

Problem Constraints
1 <= A.size() <= 10^3
1 <= A[i].size() <= 10^3
0 <= A[i][j] <= 10^3

Input Format
First argument is a 2D integer matrix A.

Output Format
Return a 2D matrix after doing required operations.

Example Input
Input 1:
[1,2,3,4]
[5,6,7,0]
[9,2,0,4]

Example Output
Output 1:
[1,2,0,0]
[0,0,0,0]
[0,0,0,0]

Example Explanation
Explanation 1:
A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.
"""


class Solution:
    def bruteforce(self, A):  # TC: O(N^3) SC: O(1)
        rows = len(A)
        for row in range(rows):
            for col in range(len(A[row])):
                if A[row][col] == 0:
                    A[row] = [0] * len(A[row])
                    for temp_row in range(rows):
                        A[temp_row][col] = 0
        return A


    #TODO

    # def optimised(self, A):  # TC: O(N^2) SC: O(N^2)
    #     rows = len(A)
    #     cols = len(A[0])
    #     first_row_has_zero = any(A[0][j] == 0 for j in range(cols))
    #     first_col_has_zero = any(A[i][0] == 0 for i in range(rows))
    #
    #     # Use first row and first column as markers
    #     for i in range(1, rows):
    #         for j in range(1, cols):
    #             if A[i][j] == 0:
    #                 A[i][0] = 0
    #                 A[0][j] = 0
    #
    #     # Zero out cells based on markers
    #     for i in range(1, rows):
    #         for j in range(1, cols):
    #             if A[i][0] == 0 or A[0][j] == 0:
    #                 A[i][j] = 0
    #
    #     # Zero out first row and column if needed
    #     if first_row_has_zero:
    #         for j in range(cols):
    #             A[0][j] = 0
    #     if first_col_has_zero:
    #         for i in range(rows):
    #             A[i][0] = 0
    #
    #     return A






if __name__ == "__main__":
    A = [[1, 2, 3, 4],
         [5, 6, 7, 0],
         [9, 2, 0, 4]]
    sol = Solution()
    print(sol.bruteforce(A))
    # print(sol.optimised(A))
