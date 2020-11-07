'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):  # time:O(nlogn) and space:O(n)
        a = []
        for i in range(len(A)):
            if A[i] > 0:
                a.append(A[i])
        a.sort()
        c = 1
        for i in a:
            if i != c:
                return c
            c += 1
        return c


# approach-2: O(n) and O(1)
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        f = -1
        # segregate an array into -ve and +ve numbers
        for i in range(len(A)):
            if A[i] <= 0:
                f += 1
                A[f], A[i] = A[i], A[f]
        l = f + 1
        A = A[l:]  # remove all negative numbers
        # print(A,l)
        for i in range(len(A)):
            if abs(A[i]) <= len(A):
                A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]  # mark positions by -ve or their presence
        c = 0
        while c < len(A):
            if A[c] > 0:
                return c + 1
            c += 1
        return c + 1
