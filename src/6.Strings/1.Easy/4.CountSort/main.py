"""
Problem Description
Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.

Problem Constraints
1 <= |A| <= 10^5
1 <= A[i] <= 10^5

Input Format
The first argument is an integer array A.

Output Format
Return an integer array that is the sorted array A.

Example Input
Input 1:
A = [1, 3, 1]
Input 2:
A = [4, 2, 1, 3]

Example Output
Output 1:
[1, 1, 3]

Output 2:
[1, 2, 3, 4]

Example Explanation
For Input 1:
The array in sorted order is [1, 1, 3].

For Input 2:
The array in sorted order is [1, 2, 3, 4].
"""
class Solution:
    def bruteforce(self):
        pass
        # commenting bruteforce as the question asks to find only using count sort.

    def optimised(self, arr):
        frequency = dict()
        min_element = 2 ** 32 - 1
        max_element = -2 ** 32
        result = list()
        for i in arr:
            min_element = min(min_element, i)
            max_element = max(max_element, i)
            frequency[i] = frequency.get(i, 0) + 1
        keys = frequency.keys()
        for i in range(min_element, max_element + 1):
            if i in keys:
                result += [i] * frequency[i]
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.optimised([4, 2, 2, 8, 3, 3, 1]))
