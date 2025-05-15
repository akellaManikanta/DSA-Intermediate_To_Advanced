"""
Problem Description

You are given an integer array A.
Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.
Return "YES" if it is possible; otherwise, return "NO" (without quotes).

Problem Constraints
1 <= |A|, A[i] <= 10^6

Input Format
The first and the only input argument is an integer array, A.

Output Format
Return a string "YES" or "NO" denoting the answer.

Example Input

Input 1:
 A = [2, 4, 8, 6]
Input 2:
 A = [2, 4, 8, 7, 6]

Example Output
Output 1:
 "YES"
Output 2:
 "NO"
"""
class Solution:
    def bruteforce(self, A):
       pass
    def optimised(self, A):
        arr_len = len(A)
        if A[0] % 2 != 0 or A[-1] % 2 != 0  or arr_len %2 != 0:
            return "NO"
        if A[0] % 2 == 0 and A[-1] % 2 == 0:
            return "YES"
        else:
            for i in range(2, arr_len, 2):
                if A[i-1]%2 == 0 or A[i]%2 == 0:
                    return "YES"
        return "NO"


if __name__ == "__main__":
    sol = Solution()
    print(sol.optimised([2, 4, 8, 6]))
    print(sol.optimised([432, 450]))
    print(sol.optimised([2, 1, 8, 6]))
    print(sol.optimised([2, 4, 8, 7, 6]))
    print(sol.optimised([978,847,95,729,778,586,188,782,813,870,871,940,312,693,580,101,760,837,564,633,680,155,241,374,682,290,850,601,433,922,773,959,530,290,990,50,516,409,868,131,664,851,721,880,20,450,745,387,787,823,392,242,674,347,65,135,819,324,651,678,139,940]))
