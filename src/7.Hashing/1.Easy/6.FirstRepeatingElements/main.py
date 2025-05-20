"""
Problem Description
Given an integer array A of size N, find the first repeating element in it.
We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
If there is no repeating element, return -1.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9

Input Format
The first and only argument is an integer array A of size N.

Output Format
Return an integer denoting the first repeating element.

Example Input
Input 1:
 A = [10, 5, 3, 4, 3, 5, 6]
Input 2:
 A = [6, 10, 5, 4, 9, 120]

Example Output
Output 1:
 5
Output 2:
 -1

Example Explanation
Explanation 1:
 5 is the first element that repeats

Explanation 2:
 There is no repeating element, output -1
"""
class Solution:
    def bruteforce(self, A):
        for i in A:
            count = 0
            for j in A:
                if i == j:
                    count += 1
                if count > 1:
                    return i
        return -1


    def optimised(self, A):
        frequency = dict()
        for i in A:
            frequency[i] = frequency.get(i, 0) + 1
        for i in A:
            if frequency[i] > 1:
                return i
        return -1



if __name__ == "__main__":
    A = [10, 5, 3, 4, 3, 5, 6]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))