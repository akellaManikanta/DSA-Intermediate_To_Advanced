"""
Problem Description
Given an array A of N integers.
Find the count of the subarrays in the array which sums to zero. Since the answer can be very large, return the remainder on dividing the result with 109+7

Problem Constraints
1 <= N <= 10^5
-109 <= A[i] <= 10^9

Input Format
Single argument which is an integer array A.

Output Format
Return an integer.

Example Input
Input 1:
 A = [1, -1, -2, 2]

Input 2:
 A = [-1, 2, -1]

Example Output
Output 1:
3
Output 2:
1

Example Explanation
Explanation 1:
 The subarrays with zero sum are [1, -1], [-2, 2] and [1, -1, -2, 2].

Explanation 2:
 The subarray with zero sum is [-1, 2, -1].

"""
class Solution:
    def bruteforce(self, A):
        len_array = len(A)
        count = 0
        for i in range(len_array):
            sum = 0
            for j in range(i, len_array):
                sum += A[j]
                if sum ==0:
                    count += 1
        return count

    def optimised(self, A):
        prefix_sum = 0
        count = 0
        frequency = dict()
        frequency[0] = 1
        for num in A:
            prefix_sum += num
            count += frequency.get(prefix_sum, 0)
            frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1
        return count



if __name__ == "__main__":
    A = [1, -1, -2, 2]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))
