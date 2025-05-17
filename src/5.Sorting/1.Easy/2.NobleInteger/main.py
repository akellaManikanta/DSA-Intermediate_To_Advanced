"""
Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

Problem Constraints
1 <= |A| <= 2*105
-10^8 <= A[i] <= 10^8

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is present else, return -1.

Example Input
Input 1:
 A = [3, 2, 1, 3]

Input 2:
 A = [1, 1, 3, 3]

Example Output
Output 1:
 1

Output 2:
 -1

Example Explanation
Explanation 1:
 For integer 2, there are 2 greater elements in the array..

Explanation 2:
 There exist no integer satisfying the required conditions.
"""


class Solution:
    def bruteforce(self, A):
        n = len(A)
        found = False

        for i in range(n):
            count = 0
            for j in range(n):
                if A[j] > A[i]:
                    count += 1
            if count == A[i]:
                found = True
                break

        return 1 if found else -1

    # First sort the array in Ascending Order to get all the greater elements than i on the right side
    # Do the calculations.
    def optimised(self, A):
        A.sort() # sorts the array
        len_array = len(A) # find the length of the array for later use
        answer = 0 # initialize the variable to find the answer.
        i = len_array - 1 # initialize the value to the last index.
        while i >= 0: # Move the pointer to the left
            if A[i] == 0 and i == len_array - 1: # Edge case if i == 0 and it's the last element.
                return 1
            if i < len_array - 1 and A[i] != A[i + 1] and A[i] == len_array - 1 - i:  # Main logic to check if elements at i and i+1 are not equal.
                answer += 1 # increment the answer as the number at index i is Noble
                # Here you can return the 1 value to caller as question asks you to find if there is at least one noble element
            while i > 0 and A[i] == A[i - 1]: # Handling the duplicate values as Noble number should be strictly greater than the elements on the right.
                i -= 1 # Decrement the value till you find a number that is not equal to itself on the left side of i.
            i -= 1 # Decrement the value of i to move to left.
        return -1 if answer == 0 else answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.bruteforce([-2,8,8,6,-2,3,-2,-7,3,3,-2,0,4,-3,-4,-2,-1,-10,-4,-2,7,-1,0,-7,3,-7,7,3,2,-4,-5,2,6,5,-2,7,-1,6,-10,4,-9,-10,-6,-2,-3,0,-2,6,-8,4,7,9,-7,9,-8,-2,-7,-10,-9,-3,8,9,1,5,4,9,2,5,-3,-6,-1,-1,-6]))
    print(sol.optimised([-2,8,8,6,-2,3,-2,-7,3,3,-2,0,4,-3,-4,-2,-1,-10,-4,-2,7,-1,0,-7,3,-7,7,3,2,-4,-5,2,6,5,-2,7,-1,6,-10,4,-9,-10,-6,-2,-3,0,-2,6,-8,4,7,9,-7,9,-8,-2,-7,-10,-9,-3,8,9,1,5,4,9,2,5,-3,-6,-1,-1,-6]))
