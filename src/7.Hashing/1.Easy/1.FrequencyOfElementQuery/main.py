"""
Problem Description
SCALER organizes a series of contests aimed at helping learners enhance their coding skills. Each learner can participate in multiple contests, and their participation is represented by integers in an array. The goal is to identify how frequently each learner has participated in these contests. This information will help SCALER determine which learners are participating the least, allowing them to provide targeted support and encouragement.

Given an array A that represents the participants of various contests, where each integer corresponds to a specific learner, and an array B containing the learners for whom you want to check participation frequency, your task is to find the frequency of each learner from array B in the array A and return a list containing all these frequencies

Problem Constraints
1 <= |A| <= 10^5
1 <= |B| <= 10^5
1 <= A[i] <= 10^5
1 <= B[i] <= 10^5

Input Format
First argument A is an array of integers.
Second argument B is an array of integers denoting the queries.

Output Format
Return an array of integers containing the frequency of each learner in B as found in array A.

Example Input
Input 1:
A = [1, 2, 1, 1]
B = [1, 2]

Input 2:
A = [2, 5, 9, 2, 8]
B = [3, 2]

Example Output
Output 1:
[3, 1]

Output 2:
[0, 2]
"""
class Solution:
    def bruteforce(self, array, elements):
        result = []
        for i in elements:
            count = 0
            for j in array:
                if i == j:
                    count += 1
            result.append(count)
        return result

    def optimised(self, array, elements):
        result = []
        frequency = dict()
        for i in array:
            frequency[i] = frequency.get(i, 0) + 1
        for i in elements:
            if i in frequency.keys():
                result.append(frequency[i])
            else:
                result.append(0)
        return result

if __name__ == "__main__":
    A = [2, 5, 9, 2, 8]
    B = [3, 2]
    sol = Solution()
    print(sol.bruteforce(A, B))
    print(sol.optimised(A, B))