"""
Problem Description
You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]

Problem Constraints
1 <= N <= 10^3
1 <= A[i] <= 10^9

Input Format
First argument A is an array of integers.

Output Format
Return an integer.

Example Input
Input 1:
A = [1, 2, 4, 3]

Input 2:
A = [2, 1, 2, 3]

Example Output
Output 1:
2

Output 2:
1

Example Explanation
For Input 1:
The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].

For Input 2:
The triplet that satisfy the conditions is [1, 2, 3].
"""
class Solution:
    def bruteforce(self, A):
        arr_length = len(A)
        count = 0
        for i in range(arr_length):
            for j in range(arr_length):
                for k in range(arr_length):
                    if i< j< k and A[i]<A[j]<A[k]:
                        count += 1
        return count

    def optimised(self, A):
        arr_length = len(A)
        count = 0
        for i in range(arr_length):
            left_count = 0
            right_count = 0
            for j in range(0, i):
                if A[i] > A[j]:
                    left_count += 1
            for k in range(i+1, arr_length):
                if A[i] < A[k]:
                    right_count += 1
            count += left_count * right_count
        return count

if __name__ == "__main__":
    A = [1, 2, 4, 3]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))