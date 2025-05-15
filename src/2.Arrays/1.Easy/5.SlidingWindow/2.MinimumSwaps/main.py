"""
Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.
Note: It is possible to swap any two elements, not necessarily consecutive.

Problem Constraints

1 <= length of the array <= 100000
-10^9 <= A[i], B <= 10^9

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the minimum number of swaps.

Example Input
Input 1:
 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8

Input 2:
 A = [5, 17, 100, 11]
 B = 20

Example Output
Output 1:
 2

Output 2:
 1

Example Explanation
Explanation 1:
 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurrence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.

Explanation 2:
 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.
"""
class Solution:
    def bruteforce(self, A, B):
        n = len(A)
        swaps = 0
        for i in range(n):
            for j in range(i+1,n):
                if A[i] > B >= A[j]:
                    print(A[i], A[j])
                    A[i], A[j] = A[j], A[i]
                    swaps += 1
                    break
        return swaps

    def optimised(self, A, B):
        n = len(A)
        # print(A)
        window_size = sum([1 for i in A if i <= B])        # calculate good elements in first 3 elements.
        min_swaps = 2**32-1
        good = 0
        for i in range(window_size):
            if A[i]<=B:
                good += 1
        min_swaps = min(min_swaps, window_size - good)
        # print(f"good elements in {A[:window_size]} are {good} and no of swaps = {min_swaps}")
        for i in range(1, n-window_size+1):
            if A[i-1] <= B:
                good -= 1
            if A[i+window_size-1] <= B:
                good += 1
            min_swaps = min(min_swaps, window_size - good)
            # print(f"good elements in {A[i:i+window_size]} are {good} and no of swaps = {min_swaps}")

        return min_swaps


if __name__ == "__main__":
    A = [1, 12, 10, 3, 14, 10, 5]
    B = 8
    sol = Solution()
    print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))