"""
Problem Description
Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B.

Problem Constraints
 1 <= length of the array <= 50000
-1000 <= A[i] <= 1000

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the total number of subarrays having sum equals to B.

Example Input
Input 1:
A = [1, 0, 1]
B = 1

Input 2:
A = [0, 0, 0]
B = 0

Example Output
Output 1:
4

Output 2:
6

Example Explanation
Explanation 1:
[1], [1, 0], [0, 1] and [1] are four subarrays having sum 1.

Explanation 1:
All the possible subarrays having sum 0.
"""
from collections import defaultdict


class Solution:
    def bruteforce(self,A, B):
        arr_len = len(A)
        count = 0
        for i in range(arr_len):
            sub_array_sum = 0
            for j in range(i, arr_len):
                sub_array_sum += A[j]
                if sub_array_sum == B:
                    count += 1
        return count

    def optimised(self, A, B):
        prefix_sum = 0
        count = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1

        for number in A:
            prefix_sum += number
            if prefix_sum -B in sum_freq:
                count += sum_freq[prefix_sum -B]
            sum_freq[prefix_sum] += 1

        return count


if __name__ == "__main__":
    A = [1, 1, 1]
    B = 2
    sol = Solution()
    print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))