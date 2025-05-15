"""
Given an integer array A containing N distinct integers, you have to find all the leaders in array A.
An element is a leader if it is strictly greater than all the elements to its right side.
NOTE: The rightmost element is always a leader.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 108

Input Format
There is a single input argument which a integer array A

Output Format
Return an integer array denoting all the leader elements of the array.

Example Input
Input 1:
A = [16, 17, 4, 3, 5, 2]

Input 2:
A = [5, 4]

Example Output
Output 1:
[17, 2, 5]

Output 2:
[5, 4]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def bruteforce(self, A):  # TC: O(N^2) SC:O(1)
        n = len(A)
        length = n
        min_element = max_element = A[0]
        for i in range(1, n):
            if A[i] > max_element:
                max_element = A[i]
            if A[i] < min_element:
                min_element = A[i]
        for i in range(n):
            if A[i] == min_element:
                # check on left for the max_element
                for j in range(i - 1, -1, -1):
                    if A[j] == max_element:
                        length = min(length, i - j + 1)
                for j in range(i + 1, length):
                    if A[j] == max_element:
                        length = min(length, j - i + 1)
            if A[i] == max_element:
                # check on right for the min_element
                for j in range(i - 1, -1, -1):
                    if A[j] == min_element:
                        length = min(length, i - j + 1)
                for j in range(i + 1, n):
                    if A[j] == min_element:
                        length = min(length, j - i + 1)
        return length

    def optimised(self, A):  # TC: O(N), SC: O(1)
        n = len(A)
        min_element = max_element = A[0]

        for i in range(1, n):
            min_element = min(min_element, A[i])
            max_element = max(max_element, A[i])

        if min_element == max_element:
            return 1  # all elements are equal

        min_index = max_index = -1
        length = n

        for i in range(n):
            if A[i] == min_element:
                min_index = i
                if max_index != -1:
                    length = min(length, abs(max_index - min_index) + 1)
            if A[i] == max_element:
                max_index = i
                if min_index != -1:
                    length = min(length, abs(max_index - min_index) + 1)

        return length


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([377,448,173,307,108]))
    print(sol.optimised([377,448,173,307,108]))
