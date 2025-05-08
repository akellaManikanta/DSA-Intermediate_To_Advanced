"""
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

Problem Constraints
1 <= |A| <= 10^5
0 <= A[i] <= 10^9

Input Format
The first argument is an integer array A.
"""
class Solution:
    def bruteforce_an_optimised(self, A): # TC: O(N) SC: O(1)
        max_element = -2 ** 32
        second_max = -2 ** 32
        for i in range(0, len(A)):
            if A[i] > max_element:
                max_element = A[i]

        for i in range(0, len(A)):
            if A[i] != max_element and A[i] > second_max:
                second_max = A[i]
        return second_max if second_max != -2 ** 32 else -1

    def more_optimised(self, A): # TC: O(N) SC: O(1)
        if len(A) < 2:
            return -1
        first = second = -2 ** 32
        for num in A:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num
        if second == -2 ** 32:
            return -1
        return second

if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce_an_optimised([1,2,3,4]))
    print(sol.more_optimised([1,2,3,4]))

