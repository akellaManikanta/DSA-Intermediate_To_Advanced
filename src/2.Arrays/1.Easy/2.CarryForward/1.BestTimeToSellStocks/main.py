"""
Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Return the maximum possible profit.

Problem Constraints
0 <= len(A) <= 7e5
1 <= A[i] <= 1e7

Input Format
The first and the only argument is an array of integers, A.

Output Format
Return an integer, representing the maximum possible profit.

Example Input
Input 1:

 A = [1, 2]

Input 2:

 A = [1, 4, 5, 2, 4]

Example Output
Output 1:
 1

Output 2:
 4
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def bruteforce(self, arr):
        max_profit = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                max_profit = max(max_profit, arr[j] - arr[i])
        return max_profit

    def optimised(self, arr):
        min_price = arr[0]
        max_price = arr[0]
        max_profit = 0
        for i in range(len(arr)):
            if arr[i] < min_price:
                min_price = arr[i]
            if arr[i] > max_price:
                max_price = arr[i]
            max_profit = max(max_profit, max_price - min_price)
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([1, 2]))
    print(sol.optimised([1, 2]))
    print(sol.bruteforce([1, 4, 5, 2, 4]))
    print(sol.optimised([1, 4, 5, 2, 4]))

