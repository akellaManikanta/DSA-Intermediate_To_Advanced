"""
Given two integers A and B. A represents the count of mangoes and B represent the count of slices of mangoes.
Mango can be cut into three slices of mangoes. A glass of mango shake can be formed by two slices of mangoes.
Find the maximum number of glasses of mango shakes you can make with A mangoes and B slices of mangoes initially.

Input Format
The First argument is an integer A.
The Second argument is an integer B.

Output Format

Return the maximum number of glasses of mango shakes you can make.

Constraints

0 <= A, B <= 10^8

For Example

Input 1:
    A = 19
    B = 0
Output 1:
    28

Input 2:
    A = 7
    B = 1
Output 2:
    11
"""

class Solution:
    def juices(self, A, B):
        total_no_of_slices = 3 * A + B # A mangoes with B initial Slices
        return total_no_of_slices // 2 # total number of glasses.

if __name__ == "__main__":
    sol = Solution()
    print(sol.juices(19, 0))
    print(sol.juices(7, 1))