"""
Problem Description
Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <=10^9
1 <= B <= 10^9

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def bruteforce(self, A, B):
        for i in range(B%len(A)):
            A.insert(0, A[-1])
            A.pop(len(A)-1)
        return A

    def optimised(self, A, B):
        len_arr = len(A)
        no_of_rotations = B % len_arr
        if no_of_rotations == 0 or len_arr == 1:
            return A
        def reverse_arr(array, start, end):
            while start <= end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
            return None

        # Rotate the complete array
        reverse_arr(A, 0, len_arr-1)
        # rotate the array from 0 till B-1 indices
        reverse_arr(A, 0, B-1)
        # rotate the array from B till len(A) - 1 indices
        reverse_arr(A, B, len_arr-1)
        return A

if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([1,2,3,4], 2))
    print(sol.optimised([1,2,3,4], 2))