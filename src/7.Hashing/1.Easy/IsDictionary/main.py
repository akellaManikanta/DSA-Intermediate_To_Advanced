"""
Problem Description
Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

Problem Constraints
1 <= N, length of each word <= 105
Sum of the length of all words <= 2 * 106

Input Format
The first argument is a string array A of size N.
The second argument is a string B of size 26, denoting the order.

Output Format
Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

Example Input
Input 1:
 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"

Input 2:
 A = ["fine", "none", "bush"]
 B = "qwertyuiopasdfghjklzxcvbnm"

Example Output
Output 1:
 1

Output 2:
 0
"""
class Solution:
    def bruteforce(self, A, B:str):
        len_A = len(A)

        for i in range(len_A-1):
            is_in_order = False
            for j in range(len(A[i])):
                print(A[i][j], A[i+1][j], B.index(A[i][j]), B.index(A[i+1][j]))
                if B.index(A[i][j]) < B.index(A[i+1][j]):
                    is_in_order = True
                return 0 if is_in_order == False else 1
        return 0

    def optimised(self, A:list[str], B:str):
        # Create a mapping of each character to its index in the alien alphabet
        frequency = {char: idx for idx, char in enumerate(B)}

        # Compare each word with the next one in the list
        for i in range(len(A) - 1):
            word1 = A[i]
            word2 = A[i + 1]

            # Compare characters of both words
            for c1, c2 in zip(word1, word2):
                if frequency[c1] < frequency[c2]:
                    # word1 < word2, so far so good
                    break
                elif frequency[c1] > frequency[c2]:
                    # word1 > word2 => not sorted
                    return 0
            else:
                # If we compared all letters and they were equal,
                # check if word1 is longer than word2, which is not allowed
                if len(word1) > len(word2):
                    return 0

        return 1

if __name__ == "__main__":
    A = ["fine", "none", "no"]
    B = "qwertyuiopasdfghjklzxcvbnm"
    sol = Solution()
    # print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))
