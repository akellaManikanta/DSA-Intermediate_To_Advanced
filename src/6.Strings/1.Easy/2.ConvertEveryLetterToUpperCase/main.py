"""
Problem Description

You are given a function to_upper() consisting of a character array A.
Convert each character of A into Uppercase character if it exists.
If the Uppercase of a character does not exist, it remains unmodified.
The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
Return the uppercase version of the given character array.

Problem Constraints
1 <= |A| <= 10^5

Input Format
Only argument is a character array A.

Output Format
Return the uppercase version of the given character array.

Example Input
Input 1:
 A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
Input 2:
 A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']

Example Output
Output 1:
 ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']
Output 2:
 ['S', 'C', 'A', 'L', 'E', 'R', '#', '2', '0', '2', '0']

Example Explanation
Explanation 1:
 All the characters in the returned array are in uppercase alphabets.

Explanation 2:
 Since there is no Uppercase version for '#', '2'and '0'.  It remains unchanged.
 Rest of the Lowercase alphabets are converted to Uppercase accordingly.
"""
class Solution:
    def bruteforce(self, A):
        result = []
        for char in A:
            # Check if character is lowercase (a-z)
            if 'a' <= char <= 'z':
                # Convert to uppercase by subtracting 32 to ASCII value
                lower_char = chr(ord(char) - 32)
                result.append(lower_char)
            else:
                # Keep character as is
                result.append(char)
        return result

    def optimised(self, A):
        return [i.upper() for i in A]

if __name__ == "__main__":
    A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))