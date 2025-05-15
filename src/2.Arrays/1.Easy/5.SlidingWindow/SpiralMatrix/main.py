"""
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.

Problem Constraints
1 <= A <= 1000
Input Format
First and only argument is integer A

Output Format
Return a 2-D matrix which consists of the elements added in spiral order.

Example Input
Input 1:
1

Input 2:
2

Input 3:
5

Example Output

Output 1:
[ [1] ]

Output 2:
[ [1, 2],
  [4, 3] ]

Output 3:
[ [1,   2,  3,  4, 5],
  [16, 17, 18, 19, 6],
  [15, 24, 25, 20, 7],
  [14, 23, 22, 21, 8],
  [13, 12, 11, 10, 9] ]
"""
class Solution:
    def bruteforce(self, n):
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # Left to right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1

            # Top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Right to left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1

            # Bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce(4))
