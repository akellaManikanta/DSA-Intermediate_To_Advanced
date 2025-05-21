"""
Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R,
such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.
Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R.
If there are multiple solutions, return the lexicographically smallest pair of L and R.
NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

Problem Constraints
1 <= size of string <= 100000

Input Format
First and only argument is a string A.

Output Format
Return an array of integers denoting the answer.

Example Input
Input 1:
A = "010"
Input 2:
A = "111"

Example Output
Output 1:
[1, 1]

Output 2:
[]

Example Explanation
Explanation 1:

A = "010"
Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
"""
class Solution:
    def bruteforce(self, A):
        n = len(A)
        max_gain = 0
        best_L = -1
        best_R = -1

        for L in range(n):
            for R in range(L, n):
                gain = 0
                for k in range(L, R + 1):
                    if A[k] == '0':
                        gain += 1  # flipping 0 to 1
                    else:
                        gain -= 1  # flipping 1 to 0

                if gain > max_gain:
                    max_gain = gain
                    best_L, best_R = L, R

        if max_gain == 0:
            return []  # No beneficial flip found
        else:
            return [best_L + 1, best_R + 1]

    def optimised(self, A):
        max_sum = 0
        current_sum = 0
        start = 0
        best_l = -1
        best_r = -1

        for i, ch in enumerate(A):
            val = 1 if ch == '0' else -1
            current_sum += val

            if current_sum < 0:
                current_sum = 0
                start = i + 1
            elif current_sum > max_sum:
                max_sum = current_sum
                best_l = start
                best_r = i

        if best_l == -1:
            return []  # No beneficial flip
        else:
            # Return 1-based indices
            return [best_l + 1, best_r + 1]


if __name__ == "__main__":
    A = "010"
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))