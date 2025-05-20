"""
Problem Description
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.

Problem Constraints
1 <= N <= 10^5
A[i] ∈ ['a'-'z', 'A'-'Z']

Input Format
First and only argument is a character string A.

Output Format
Return a character string.

Example Input
Input 1:
 A = "Hello"
Input 2:
 A = "tHiSiSaStRiNg"

Example Output
Output 1:
 hELLO

Output 2:
 ThIsIsAsTrInG

Example Explanation
Explanation 1:
 'H' changes to 'h'
 'e' changes to 'E'
 'l' changes to 'L'
 'l' changes to 'L'
 'o' changes to 'O'

Explanation 2:
 "tHiSiSaStRiNg" changes to "ThIsIsAsTrInG".
"""
class Solution:
    def bruteforce(self, A):
        result = ""
        for i in A:
            if 'a' <= i <= 'z':
                # Convert to uppercase by subtracting 32 to ASCII value
                result += chr(ord(i) - 32)
            elif 'A' <= i <= 'Z':
                # Convert to lowercase by adding 32 to ASCII value
                result += chr(ord(i) + 32)
            else:
                pass
        return result

    def optimised(self, A):
        result = ""
        for index, value in enumerate(A):
            if value.islower():
                result += value.upper()
            if value.isupper():
                result += value.lower()
        return result

if __name__ == "__main__":
    A = "Hello"
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))