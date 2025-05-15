"""
Problem Description
Given an array B of length A with elements 1 or 0. Find the number of subarrays such that the bitwise OR of all the elements present in the subarray is 1.
Note : The answer can be large. So, return type must be long.

Problem Constraints
1 <= A <= 105

Input Format
The first argument is a single integer A.
The second argument is an integer array B.

Output Format
Return the number of subarrays with bitwise array 1.

Example Input
Input 1:
 A = 3
B = [1, 0, 1]
Input 2:
 A = 2
B = [1, 0]

Example Output
Output 1:
5
Output2:
2
"""
class Solution:
    def bruteforce(self, length:int, array:list[int]):
        answer = 0
        for i in range(length):
            sum = 0
            for j in range(i, length):
                sum |= array[j]
                if sum == 1:
                    answer += 1
        return answer

    def optimised(self, length:int, array:list[int]):
        total_subarrays = length * (length + 1) // 2
        zero_subarrays = 0
        i = 0
        while i < length:  # iterate through the end of the list
            if array[i] == 0: # check if element is zero
                j = i # assigning j to i to check how many zero are continuous
                while j < length and array[j] == 0: # move forward till you find the 1 again
                    j += 1
                length = j - i # length of arrays with adjacent zeros
                zero_subarrays += (length * (length + 1)) // 2 # total sub arrays to eliminate.
                i = j # assign the i to the j to move forward with ones again.
            else:
                i += 1
        return total_subarrays - zero_subarrays


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce(3, [1,0,1]))
    # print(sol.bruteforce(3, [1,0,1]))
