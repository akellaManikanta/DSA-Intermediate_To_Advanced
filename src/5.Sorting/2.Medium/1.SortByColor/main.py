"""
Problem Description
Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.
We will represent the colors as,
red -> 0
white -> 1
blue -> 2
Note: Using the library sort function is not allowed.

Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2

Input Format
First and only argument of input contains an integer array A.

Output Format
Return an integer array in asked order

Example Input
Input 1 :
    A = [0, 1, 2, 0, 1, 2]

Input 2:
    A = [0]

Example Output
Output 1:
    [0, 0, 1, 1, 2, 2]

Output 2:
    [0]
"""

class Solution:
    def bruteforce(self, A):
        len_arr = len(A)
        for i in range(len_arr):
            for j in range(i, len_arr):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        return A

    # below solution only works as we know exactly 3 colors are present.
    def optimised(self, A):
        red = white = blue = 0
        for num in A:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        index = 0
        for _ in range(red):
            A[index] = 0
            index += 1
        for _ in range(white):
            A[index] = 1
            index += 1
        for _ in range(blue):
            A[index] = 2
            index += 1
        return A


if __name__ == "__main__":
    A = [0, 1, 2, 0, 1, 2]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))