"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
Find and return the length of the longest consecutive 1’s that can be achieved.

Input Format
The only argument given is string A.

Output Format
Return the length of the longest consecutive 1’s that can be achieved.

Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.

For Example
Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""


class Solution:
    def bruteforce(self, binary_string: str):
        longest_ones = float('-inf')
        zeros = A.count('0')
        ones = A.count('1')

        # Edge cases
        if len(A) == ones:
            return ones
        elif len(A) == zeros:
            return 0

        for i in range(len(A)):
            if A[i] == '0':
                left = 0
                right = 0

                # Count 1's to the left
                j = i - 1
                while j >= 0 and A[j] == '1':
                    left += 1
                    j -= 1

                # Count 1's to the right
                j = i + 1
                while j < len(A) and A[j] == '1':
                    right += 1
                    j += 1

                # Use the swap only if there are extra 1's outside this block
                if left + right < ones:
                    temp = left + right + 1
                else:
                    temp = left + right

                longest_ones = max(longest_ones, temp)

        return longest_ones

    def optimised(self, A: str, k=1):
        arr_length = len(A)
        max_length = 0
        left = 0
        right = 0
        zeros = 0
        total_zeros = 0
        for i in A:
            if i == '0':
                total_zeros += 1
        if total_zeros == arr_length:
            return 0

        while right < arr_length:
            if A[right] == '0':
                zeros += 1

            while zeros > k:
                if A[left] == '0':
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


if __name__ == "__main__":
    A = "0000000000000"

    sol = Solution()
    # print(sol.bruteforce(A))
    print(sol.optimised(A))
