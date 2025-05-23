"""
You are given an array A of N elements. Sort the given array in increasing order of number of
distinct factors of each element, i.e., element having the least number of factors should be the first
to be displayed and the number having highest number of factors should be the last one.
If 2 elements have same number of factors, then number with less value should come first.
Note: You cannot use any extra space

Problem Constraints
1 <= N <= 104
1 <= A[i] <= 104

Input Format
First argument A is an array of integers.

Output Format
Return an array of integers.

Example Input
Input 1:
A = [6, 8, 9]

Input 2:
A = [2, 4, 7]

Example Output
Output 1:
[9, 6, 8]

Output 2:
[2, 7, 4]
"""

class Solution:
    def bruteforce(self, A):
        pass
        # cannot do it right now as we do not know any sorting techniques
        # TODO once completed Sorting techniques.

    def optimised(self, A):
        def count_factors(number):
            i = 1
            ans = 0
            while i * i <= number:
                if number // i == i:
                    ans += 1
                elif number % i == 0:
                    ans += 2
                i += 1
            return ans
        return sorted(A, key=lambda x: (count_factors(x), x))


if __name__ == "__main__":
    A = [6, 8, 9]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))