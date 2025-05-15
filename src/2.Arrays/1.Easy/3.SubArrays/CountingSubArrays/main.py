"""
Problem Description

Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

Problem Constraints
1 <= N <= 5 x 10^3
1 <= A[i] <= 1000
1 <= B <= 10^7

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return an integer denoting the number of subarrays in A having sum less than B.

Example Input
Input 1:
 A = [2, 5, 6]
 B = 10

Input 2:
 A = [1, 11, 2, 3, 15]
 B = 10

Example Output
Output 1:
 4

Output 2:
 4

Example Explanation
Explanation 1:
 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},

Explanation 2:
 The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}
"""
class Solution:
    def bruteforce(self, array:list[int], target:int):
        len_arr = len(array)
        count = 0
        for i in range(len_arr):
            for j in range(i, len_arr):
                if sum(array[i:j+1]) < target:
                    count += 1
        return count

    def optimised(self, array:list[int], target:int):
        n = len(array)
        count = 0
        for i in range(n):
            current_sum =0
            for j in range(i, n):
                current_sum += array[j]
                if current_sum < target:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([1, 11, 2, 3, 15], 10))
    print(sol.optimised([1, 11, 2, 3, 15], 10))
