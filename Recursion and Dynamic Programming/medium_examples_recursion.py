"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

In no way, shape or form am I intending to infringe rights of the copyright holder. Content used is strictly for 
reviewing purposes. 

========================================= Examples for Recursion and Dynamic Programming =========================================
"""






# --------------------------------------------------------------------------------------------------------------------------------







"""
Problem 1: 
Given an array arr[] of length N and an integer X, the task is to find 
the number of subsets with sum equal to X using recursion.

Input: arr = [2, 3, 5, 6, 8, 10], X = 10
Output: 3
Explanation:
All possible subsets with sum 10 are [2, 3, 5], [2, 8], [10]
"""

def subsetSumCountHelper(arr, targetX, index):
    # Base case 1: if there is nothing left to check
    if(index == len(arr)): return 0

    # Base case 2: if targetX is 0 --> we found another subset --> count += 1
    if(targetX == 0): return 1

    # Base case 3: if the element we are checking is bigger than targetX --> skip that element
    if(arr[index] > targetX):
        return subsetSumCountHelper(arr, targetX, index + 1)

    # Recursive part
    # Either the element can be counted in the subset 
    # If the element is counted, then the remaining sum to be checked is sum - the selected element 
    # If the element is not included, then the remaining sum to be checked is the total sum 
    use = subsetSumCountHelper(arr, targetX - arr[index], index + 1)
    notUse = subsetSumCountHelper(arr, targetX, index + 1)

    return use + notUse

def subsetSumCount(arr, targetX):
    return subsetSumCountHelper(arr, targetX, 0)













# --------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Subset Sum Count
    input_arr = [2, 3, 5, 6, 8, 10]
    print(subsetSumCount(input_arr, 10))



