"""
Problem Description
Given an array A of length N. Also given are integers B and C.
Return 1 if there exists a subarray with length B having sum C and 0 otherwise

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^4
1 <= B <= N
1 <= C <= 10^9

Input Format
First argument A is an array of integers.
The remaining arguments B and C are integers

Output Format
Return 1 if such a subarray exist and 0 otherwise

Example Input
Input 1:
A = [4, 3, 2, 6, 1]
B = 3
C = 11

Input 2:
A = [4, 2, 2, 5, 1]
B = 4
C = 6

Example Output
Output 1:
1

Output 2:
0
"""


class Solution:
    def bruteforce(self, A, B, C):
        n = len(A)
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += A[j]
                if j - i + 1 == B and sum == C:
                    return 1
        return 0

    def optimised(self, A, B, C):
        n = len(A)
        initial_sum = sum([A[i] for i in range(B)])
        if initial_sum == C:
            return 1
        for i in range(1, n-B+1):
            initial_sum = initial_sum - A[i-1] + A[i+B-1]
            if initial_sum == C:
                return 1
        return 0


if __name__ == "__main__":
    A = [4, 3, 2, 6, 1]
    B = 3
    C = 11
    sol = Solution()
    print(sol.bruteforce(A, B, C))
    print(sol.optimised(A, B, C))
