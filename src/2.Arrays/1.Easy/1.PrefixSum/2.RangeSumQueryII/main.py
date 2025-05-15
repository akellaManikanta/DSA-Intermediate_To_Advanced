"""
Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

Problem Constraints

1 <= N, M <= 10^3
1 <= A[i] <= 10^5
0 <= L <= R < N

Input Format

The first argument is the integer array A.
The second argument is the 2D integer array B.

Output Format
Return an integer array of length M where ith element is the answer for ith query in B.

Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]

Input 2:

A = [2, 2, 2]
B = [[0, 0], [1, 2]]

Example Output
Output 1:
[10, 5]

Output 2:
[2, 4]
"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def bruteforce(self, A, B):
        arr_length = len(A)
        query_sum = []
        for index in B:
            start = index[0]
            end = index[1]
            sum = 0
            for element in range(arr_length):
                if start<=element<=end:
                    sum += A[element]
            query_sum.append(sum)
        return query_sum

    def optimised(self, A, B):
        prefix_sum = [0]*len(A)
        result = []
        for i in range(len(A)):
            if i == 0:
                prefix_sum[0] = A[0]
            else:
                prefix_sum[i] = A[i] + prefix_sum[i-1]
        for index in B:
            start = index[0]
            end = index[1]
            if start == 0:
                result.append(prefix_sum[end])
            else:
                result.append(prefix_sum[end] - prefix_sum[start-1])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([1, 2, 3, 4, 5], [[0, 3], [1, 2]]))
    print(sol.optimised([1, 2, 3, 4, 5], [[0, 3], [1, 2]]))



