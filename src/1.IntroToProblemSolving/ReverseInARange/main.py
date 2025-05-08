"""
Problem Description
Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9
0 <= B <= C <= N - 1

Input Format
The first argument A is an array of integer.
The second and third arguments are integers B and C

Output Format
Return the array A after reversing in the given range.

Example Input

Input 1:
A = [1, 2, 3, 4]
B = 2
C = 3

Input 2:
A = [2, 5, 6]
B = 0
C = 2

Example Output
Output 1:
[1, 2, 4, 3]

Output 2:
[6, 5, 2]
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def optimised(self, A, B, C):
        start = B
        end = C
        while start <= end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        return A

    def pythonic_way(self, A, B, C):
        A[B:C+1] = A[B:C+1][::-1]
        return A


if __name__ == "__main__":
    sol = Solution()
    print(sol.optimised([1, 2, 3, 4], 2, 3))
    print(sol.pythonic_way([1, 2, 3, 4], 2, 3))