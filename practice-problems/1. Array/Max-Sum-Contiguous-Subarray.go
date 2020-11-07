package Array
/*
//kadane's algorithm
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = -10000000000000
        max_ending_here = 0

        for i in range(len(A)):
            max_ending_here += A[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


*/
