"""
Problem Description
Given an integer array A containing N distinct integers.
Find the number of unique pairs of integers in the array whose XOR is equal to B.
NOTE:
    Pair (a, b) and (b, a) is considered to be the same and should be counted once.

Problem Constraints
1 <= N <= 10^5
1 <= A[i], B <= 10^7

Input Format
The first argument is an integer array A.
The second argument is an integer B.

Output Format
Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.

Example Input
Input 1:
 A = [5, 4, 10, 15, 7, 6]
 B = 5

Input 2:
 A = [3, 6, 8, 10, 15, 50]
 B = 5

Example Output
Output 1:
 1

Output 2:
 2

Example Explanation
Explanation 1:
 (10 ^ 15) = 5
Explanation 2:
 (3 ^ 6) = 5 and (10 ^ 15) = 5
"""


class Solution:
    def bruteforce(self, A, B):
        len_array = len(A)
        count = 0
        for i in range(len_array):
            for j in range(i + 1, len_array):
                if A[i] ^ A[j] == B:
                    count += 1
        return count

    def optimised(self, A, B):
        """
        If a ^ b = c, then:
        c ^ a = b
        c ^ b = a
        :param A: List of integers
        :param B: Xor Value
        :return: integer value
        """
        count = 0
        seen = set()
        used = set()
        for i in A:
            target = i ^ B
            if target in seen and (min(i, target), max(i, target)) not in used:
                count += 1
                used.add((min(i, target), max(i, target)))
            seen.add(i)
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([3, 6, 8, 10, 15, 50], 5))
    print(sol.optimised([3, 6, 8, 10, 15, 50], 5))
