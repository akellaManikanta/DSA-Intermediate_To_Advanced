"""
You are given a string S, and you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input
Only argument given is string S.

Output
Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.

Constraints
1 <= length(S) <= 1e6
S can have special characters

Example

Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.

"""
class Solution:
    def bruteforce(self,string:str):
        len_string = len(string)
        count = 0
        for i in range(len_string):
            if string[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                for j in range(i, len_string):
                    count += 1
        return count % 10003

    def optimised(self, string:str):
        len_string = len(string)
        count = 0
        for i in range(len_string):
            if string[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count += len_string - i
        return count % 10003


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce("ABEC"))
    print(sol.optimised("ABEC"))