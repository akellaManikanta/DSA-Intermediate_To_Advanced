"""
Problem Description
Given an array A of size N, find the subarray of size B with the least average.

Problem Constraints
1 <= B <= N <= 10^5
-10^5 <= A[i] <= 10^5

Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.

Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.

Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3

Input 2:
A = [3, 7, 5, 20, -10, 0, 12]
B = 2

Example Output
Output 1:
3

Output 2:
4

Example Explanation
Explanation 1:
 Subarray between indexes 3 and 5
 The subarray {20, 10, 50} has the least average
 among all subarrays of size 3.

Explanation 2:

 Subarray between [4, 5] has minimum average
"""
from zipfile import sizeEndCentDir


class Solution:
    def bruteforce(self, array: list[int], size: int):
        arr_len = len(array)
        average = 2 ** 32 - 1
        index = arr_len
        for i in range(arr_len):
            sum = 0
            for j in range(i, arr_len):
                sum += array[j]
                length = j - i + 1
                if length == size:
                    if average > sum / length:
                        average = min(average, sum / length)
                        index = i
        return index

    def optimised(self, array: list[int], size: int):
        current_sum = 0
        n = len(array)
        index = 0
        for i in range(size):
            current_sum += array[i]
        average = current_sum / size
        for i in range(1, n - size + 1):
            current_sum = current_sum - array[i - 1] + array[i + size - 1]
            current_average = current_sum / size
            if current_average < average:
                average = current_average
                index = i
        return index


if __name__ == "__main__":
    A = [18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19]
    B = 1
    sol = Solution()
    print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))
