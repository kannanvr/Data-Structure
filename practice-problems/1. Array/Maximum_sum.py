"""
maximum sum such that no two elements are adjacent
"""


def maxPizza(n, a):
    incl = excl = 0
    for i in a:
        tmp = max(incl, excl)
        incl = excl + i
        excl = tmp
    return max(incl, excl)


'''
Largest Sum Contiguous Subarray
'''


def maxSubArray(self, A):
    max_so_far = -10000000000000
    max_ending_here = 0

    for i in range(len(A)):
        max_ending_here += A[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


'''
Find the length of largest subarray with 0 sum

'''


def maxLen(arr):
    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}
    # Initialize result
    max_len = 0
    # Initialize sum of elements
    curr_sum = 0
    # Traverse through the given array
    for i in range(len(arr)):
        # Add the current element to the sum
        curr_sum += arr[i]
        if arr[i] is 0 and max_len is 0:
            max_len = 1
        if curr_sum is 0:
            max_len = i + 1
        # NOTE: 'in' operation in dictionary to search
        # key takes O(1). Look if current sum is seen
        # before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            # else put this sum in dictionary
            hash_map[curr_sum] = i
    return max_len
