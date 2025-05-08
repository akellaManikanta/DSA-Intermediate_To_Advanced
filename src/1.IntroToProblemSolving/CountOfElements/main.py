"""
Problem Description
Given an array A of N integers.
Count the number of elements that have at least 1 elements greater than itself.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First and only argument is an array of integers A.

Output Format
Return the count of elements.

Example Input
Input 1:
A = [3, 1, 2]

Input 2:
A = [5, 5, 3]

Example Output
Output 1:
    2

Output 2:
    1
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def bruteforce(self, A): # TC O(N^2) SC:O(1)
        count = 0
        arr_len = len(A)
        for i in range(arr_len):
            for j in range(i+1, arr_len):
                if A[i] > A[j]:
                    count += 1
                    break
        return count

    def optimised(self, A): # TC: O(N) SC: O(1)
        largest_element = -2**32
        count = 0
        arr_len = len(A)
        for i in range(arr_len):
            largest_element = max(largest_element, A[i])
        for i in range(arr_len):
            if A[i] != largest_element:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([3,5,3,2,9,3,10,10,10,3]))
    print(sol.optimised([3,5,3,2,9,3,10,10,10,3]))
