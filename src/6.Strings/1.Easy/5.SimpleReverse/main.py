"""
Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.

Problem Constraints
1 <= |A| <= 10^5
String A consist only of lowercase characters.

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the reversed string.

Example Input
Input 1:
 A = "scaler"
Input 2:
 A = "academy"

Example Output
Output 1:
 "relacs"

Output 2:
 "ymedaca"

Example Explanation
Explanation 1:
 Reverse the given string.
"""
class Solution:
    def bruteforce(self, string):
        reverse = ""
        for i in string:
            reverse += i
        return reverse

    def optimised(self, string):
        return string[::-1]

if __name__ == "__main__":
    A = "scaler"
    sol = Solution()
    sol.bruteforce(A)
    sol.optimised(A)