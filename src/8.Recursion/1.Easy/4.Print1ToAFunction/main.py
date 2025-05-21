"""
Problem Description
You are given an integer A, print 1 to A using using recursion.
Note :- After printing all the numbers from 1 to A, print a new line.

Problem Constraints
1 <= A <= 10^4

Input Format
First argument A is an integer.

Output Format
Print A space-separated integers 1 to A.
Note: There should be exactly one space after each integer. After printing all the integers, print a new line

Example Input
Input 1:
A = 10
Input 2:
A = 5

Example Output
Output 1:
1 2 3 4 5 6 7 8 9 10

Output 2:
1 2 3 4 5

Example Explanation
Explanation 1:
Print 1 to 10 space separated integers.

Explanation 2:
Print 1 to 5 space separated integers.
"""
class Solution:
    def print_function1(self, A):
        def p1(A):
            if A==0:
                return
            p1(A-1)
            print(A,end=" ")
        p1(A)
        print()

    def print_function2(self, A):
        def p1(A):
            if A==0:
                return
            print(A,end=" ")
            p1(A-1)

        p1(A)
        print()


if __name__ == "__main__":
    A = 10
    sol = Solution()
    sol.print_function1(A) # 1 2 3 4 5 6 7 8 9 10
    sol.print_function2(A) # 10 9 8 7 6 5 4 3 2 1