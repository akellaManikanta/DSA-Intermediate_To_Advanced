"""
Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints
0 <= sum of length of all strings <= 1000000

Input Format
The only argument given is an array of strings A.

Output Format
Return the longest common prefix of all strings in A.

Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]

Input 2:
A = ["abab", "ab", "abcd"];

Example Output
Output 1:
"a"

Output 2:
"ab"

Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".

Explanation 2:
Longest common prefix of all the strings is "ab".
"""


class Solution:
    def bruteforce(self, strings):
        #TODO
        pass


    def optimised(self, strings):
        prefix = ""
        min_string = None
        for i in range(len(strings)):
            if i == 0:
                min_string = len(strings[i])
            else:
                min_string = min_string if min_string < len(strings[i]) else len(strings[i])
            # print(i, min_string)
        inital_string = [] if strings is [] else strings[0]
        for i in range(min_string):
            if set(inital_string[i]) == set(elem[i] for elem in strings):
                prefix += inital_string[i]
            else:
                break
        return prefix


if __name__ == "__main__":
    A = ["abcdefgh", "aefghijk", "abcefgh"]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))