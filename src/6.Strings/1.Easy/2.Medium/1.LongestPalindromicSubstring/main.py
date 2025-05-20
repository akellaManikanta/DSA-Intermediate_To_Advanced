"""
Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).

Problem Constraints
1 <= N <= 6000

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the longest palindromic substring of string A.

Example Input
Input 1:
A = "aaaabaaa"
Input 2:
A = "abba

Example Output
Output 1:
"aaabaaa"
Output 2:
"abba"

Example Explanation
Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".
"""


class Solution:
    def bruteforce(self):
        pass

    def optimised(self, s):
        if not s:
            return ""
        longest = ""
        for i in range(len(s)):
            palindrome_odd = self.expand_around_center(s, i, i)
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd

            palindrome_even = self.expand_around_center(s, i, i + 1)
            if len(palindrome_even) > len(longest):
                longest = palindrome_even

        return longest

    def expand_around_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


if __name__ == "__main__":
    pass
