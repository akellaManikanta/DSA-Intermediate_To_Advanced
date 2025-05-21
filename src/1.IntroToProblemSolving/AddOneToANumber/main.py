"""
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :
    Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
    A: For the purpose of this question, YES
    Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
    A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

Problem Constraints
1 <= size of the array <= 1000000

Input Format
First argument is an array of digits.

Output Format
Return the array of digits after adding one.
Example Input
Input 1:
[1, 2, 3]

Example Output
Output 1:
[1, 2, 4]

Example Explanation
Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""
class Solution:
    def bruteforce(self, A):
        while len(A) > 1 and A[0] == 0:
            A.pop(0)

        len_array = len(A)
        carry = 0
        result = []

        for i in range(len_array - 1, -1, -1):
            if i == len_array - 1:
                # Add 1 to the last digit
                current_sum = A[i] + 1
            else:
                current_sum = carry + A[i]

            carry = current_sum // 10
            current_sum = current_sum % 10

            result.append(current_sum)

        if carry == 1:
            result.append(1)

        return result[::-1]

    def optimised(self, A):
        pass

if __name__ == "__main__":
    A = [0,3,7,6,4,0,5,5,5]
    sol = Solution()
    print(sol.bruteforce(A))
    print(sol.optimised(A))