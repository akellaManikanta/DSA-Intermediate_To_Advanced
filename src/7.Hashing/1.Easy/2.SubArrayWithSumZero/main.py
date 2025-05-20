"""
Problem Description
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

Problem Constraints

1 <= |A| <= 100000

-10^9 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.

Output Format
Return whether the given array contains a subarray with a sum equal to 0.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [4, -1, 1]

Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 No subarray has sum 0.

Explanation 2:
 The subarray [-1, 1] has sum 0.
"""

class Solution:
    def bruteforce(self, array):
        len_array = len(array)
        for i in range(len_array):
            sum = 0
            for j in range(i, len_array):
                sum += array[j]
                if sum == 0:
                    return 1
        return 0

    def optimised(self, array):
        frequency = set()
        sum = 0
        for i in array:
            if sum == 0 or sum in frequency:
                return 1
            else:
                frequency.add(sum)
        return 0


if __name__ == "__main__":
    A = [4, 1, -1]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))
