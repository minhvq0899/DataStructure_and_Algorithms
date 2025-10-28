"""
Google final round technical interview.

Given an array that can contain negative element, find the pair of index (i,j) such that arr[i] == arr[j] and i <= j and
the sum of the subarray[i:j+1] is maximized.

Constraints: 
0 <= len(arr) <= 10^5
10^5 < arr[i] < 10^5
"""

from typing import List
from collections import defaultdict

# Given an array (len n), return the prefixSum array (len n+1) of the input array
# With the prefixSum array, we can compute the sum of any subarray [i: j+1] n O(1) if we know i and j 
def computePrefixSum(arr: List[int]) -> List[int]: 
    n = len(arr)
    prefixSum = [0] * (n+1)
    for i in range(n):
        prefixSum[i+1] = arr[i] + prefixSum[i]

    # print(prefixSum)
    return prefixSum


# Main function
def maximizedSumSubArray(arr: List[int]) -> List[int]:
    # Compute Prefix sum array - O(N)
    n = len(arr)
    prefix_sum = computePrefixSum(arr)

    value_to_indices = defaultdict(list)            # key: each element -> value: list of indices this element appears before i
    max_sum = float('-inf')
    best_pair = (-1, -1)

    # O(N^2)
    for i in range(n):
        val = arr[i]

        # Examine each indice that val has appeared before
        for j in value_to_indices[val] + [i]:  # include i itself
            sub_sum = prefix_sum[i + 1] - prefix_sum[j]
            if sub_sum > max_sum:
                max_sum = sub_sum
                best_pair = (j, i)

        # Add this value to indices dict
        value_to_indices[val].append(i)

    print("best_pair: ", best_pair)
    return best_pair




"""
        0    1   2  3  4   5
arr1 = [3, -100, 3, 4, -1, 3]
maximizedSumSubArray(arr1) -> [0,5]

"""
arr1 = [3, -100, 3, 4, -1, 3]
# maximizedSumSubArray(arr1)

computePrefixSum(arr1)