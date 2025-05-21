"""
Problem Description
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.
Note: A palindrome is a string that's the same when read forward and backward.

Problem Constraints
1 <= |A| <= 50000
String A consists only of lowercase letters.

Input Format
The first and only argument is a string A.

Output Format
Return 1 if the string A is a palindrome, else return 0.

Example Input
Input 1:
 A = "naman"
Input 2:
 A = "strings"

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 "naman" is a palindomic string, so return 1.

Explanation 2:
 "strings" is not a palindrome, so return 0.
"""
class Solution:
    def bruteforce(self, string):
        rev_string = self.reverse_string(string)
        return 1 if rev_string == string else 0

    def reverse_string(self, string): # this will only work for small strings
        len_string = len(string)
        if len_string == 1:
            return string
        else:
            string_rev = str(string[-1]) + str(self.reverse_string(string[:len_string-1])) # not an accepted solution as slicing take O(N) time complexity
            return string_rev

    def optimised(self, string):
        def reverse_helper(s, left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return reverse_helper(s, left + 1, right - 1)

        return 1 if reverse_helper(string, 0, len(string) - 1) else 0

if __name__ == "__main__":
    A = "naman"
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))
