"""
Problem Description

You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

Note:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.

Problem Constraints

1 <= N <= 10^5
-105 <= A[i] <= 10^5

Input Format
First arugment is an array A .

Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.

Example Input
Input 1:
A = [-7, 1, 5, 2, -4, 3, 0]
Input 2:
A = [1, 2, 3]

Example Output
Output 1:
3

Output 2:
-1
"""
class Solution:
    def calculate_sum(self, arr, start_index, end_index):
        sum = 0
        for i in range(start_index, end_index):
            sum += arr[i]
        return sum

    def bruteforce(self, A): # TC: O(N^2), SC: O(1)
        len_arr = len(A)
        for i in range(len_arr):
            left_sub_array_sum = 0
            right_sub_array_sum = 0
            if i == 0:
                right_sub_array_sum = self.calculate_sum(A, i + 1, len_arr)
            elif i == len_arr:
                left_sub_array_sum = self.calculate_sum(A, 0, len_arr)
            else:
                left_sub_array_sum = self.calculate_sum(A, 0, i)
                right_sub_array_sum = self.calculate_sum(A, i + 1, len_arr)
            if left_sub_array_sum == right_sub_array_sum:
                return i
        return -1

    def optimised(self, A): # TC: O(N), SC: O(N), Can also be done via TC: O(N) and O(1) using carry forward technique.
        arr_length = len(A)
        prefix_sum = [0]*len(A)
        for i in range(arr_length):
            if i == 0:
                prefix_sum[i] = A[0]
            else:
                prefix_sum[i] = prefix_sum[i-1] + A[i]
        for i in range(arr_length):
            if i == 0:
                left_sub_array_sum = 0
                right_sub_array_sum = prefix_sum[arr_length-1] - prefix_sum[i]
            else:
                left_sub_array_sum = prefix_sum[i-1]
                right_sub_array_sum = prefix_sum[arr_length-1] - prefix_sum[i]
            if left_sub_array_sum == right_sub_array_sum:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([-7, 1, 5, 2, -4, 3, 0]))
    print(sol.optimised([-7, 1, 5, 2, -4, 3, 0]))
