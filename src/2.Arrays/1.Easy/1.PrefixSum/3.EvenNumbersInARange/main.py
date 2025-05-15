"""
Problem Description

You are given an array A of length N and Q queries given by the 2D array B of size Q×2.
Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].

Problem Constraints
1 <= N <= 105
1 <= Q <= 105
1 <= A[i] <= 109
0 <= B[i][0] <= B[i][1] < N

Input Format
First argument A is an array of integers.
Second argument B is a 2D array of integers.

Output Format
Return an array of integers.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [   [0, 2]
        [2, 4]
        [1, 4]   ]

Input 2:
A = [2, 1, 8, 3, 9, 6]
B = [   [0, 3]
        [3, 5]
        [1, 3]
        [2, 4]   ]

Example Output
Output 1:
[1, 1, 2]

Output 2:
[2, 1, 1, 1]

"""
from sys import prefix


class Solution:
    def bruteforce(self, array: list[int], ranges: list[list[int]]): # TC: O(N), SC: O(1)
        counts = []
        for cur_range in ranges:
            start = cur_range[0]
            end = cur_range[1]
            count = 0
            for i in range(start, end + 1):
                if array[i] % 2 == 0:
                    count += 1
            counts.append(count)
        return counts

    def optimised(self, array: list[int], ranges: list[list[int]]):
        len_arr = len(array)
        prefix_sum = [0]* len_arr
        result = []
        for i in range(len_arr):
            if A[i] % 2 == 0:
                if i == 0:
                    prefix_sum[i] = 1
                else:
                  prefix_sum[i] = prefix_sum[i-1] + 1
            else:
                if i == 0:
                    prefix_sum[i] = 0
                else:
                    prefix_sum[i] = prefix_sum[i-1]
        for index in B:
            start = index[0]
            end = index[1]
            if start == 0:
                result.append(prefix_sum[end])
            else:
                result.append(prefix_sum[end] - prefix_sum[start-1])
        return result


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [[0, 2],
         [2, 4],
         [1, 4]]
    sol = Solution()
    print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))
