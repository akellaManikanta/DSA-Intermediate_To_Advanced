"""
Problem Description
You are given an array A of N integers and an integer B. Count the number of pairs (i,j) such that A[i] + A[j] = B and i ≠ j.
Since the answer can be very large, return the remainder after dividing the count with 109+7.
Note - The pair (i,j) is same as the pair (j,i) and we need to count it only once.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format
First argument A is an array of integers and second argument B is an integer.

Output Format
Return an integer.

Example Input
Input 1:
A = [3, 5, 1, 2]
B = 8
Input 2:
A = [1, 2, 1, 2]
B = 3

Example Output
Output 1:
1
Output 2:
4

Example Explanation
Example 1:
The only pair is (1, 2) which gives sum 8

Example 2:
The pair which gives sum as 3 are (1, 2), (1, 4), (2, 3) and (3, 4).
"""
from collections import defaultdict


class Solution:
    def bruteforce(self, A, B):
        len_array = len(A)
        for i in range(len_array):
            for j in range(i+1, len_array):
                if i != j and A[i] + A[j] == B:
                    return 1
        return 0

    def optimised(self, arr, k):
        frequency = defaultdict(int)
        for num in arr:
            if (k - num) in frequency:
                return 1
            frequency[num] += 1
        return 0




if __name__ == "__main__":
    A = arr = [46,59,55,61,28,13,22,18,26,18,31,95,91,95,21,95,0,67,64,84,25,12,98,67,24,67,99,29,26,49,73,77,79,77,80,39,68,36,35,72,45,60,58,83,98,10,95,5,40,6,99,81,19,38,75,4,25,91,1,24,52,56,30,43,1,46,87,30,23,73,40,13,81,31,75,31,21,52,62,29,58,97,0,42,6,44,56,11,14,59,96,91,53,23,25,19,99,81,25,53,85,53,46,76,31,29,97,64,16,70,36,95,27,52,37,81,48,71,83,21,56,78,1,88,30,97,80,87,43,27,43,29,10,7,28,34,51,34,0,26,13,39,23,64,92,34,8,73,45,2,10,9,81,69,65,6,81,41,40,24,77,10,40,17,76,16,67,25,24,17,14,90,10,50,90,41,57,33,47,65,27,68,47,2,36,82,76,64,12,59,32,42,56,76,1,21,47,56,84,63]
    B = 0
    sol = Solution()
    print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))