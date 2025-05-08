"""
Problem Description

Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.

Problem Constraints

1 <= A.size() <= 10^4
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return 1 if good pair exist otherwise return 0.

Example
Input 1:
A = [1,2,3,4]
B = 7

Input 2:
A = [1,2,4]
B = 4

Input 3:
A = [1,2,2]
B = 4
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bruteforce(self, A, B):
        arr_len = len(A)
        for i in range(arr_len):
            for j in range(arr_len):
                if i != j and A[i] + A[j] == B:
                    return 1
        return 0

    def optimised(self, A:list, B):
        for index, value in enumerate(A):
            other_number = B - value
            if other_number in A and A.index(other_number) != index:
                return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([1,2,3,4], 7))
    print(sol.optimised([1,2,3,4], 7))