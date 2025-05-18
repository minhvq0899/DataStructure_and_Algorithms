"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

===================================== Leetcode exercises for Hash Table =====================================

"""
from typing import List

class leetcode442:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        # hash each element
        for i in range (len(nums)):
            print(i, "  ", nums[nums[i] - 1])
            nums[nums[i] - 1] += len(nums) 
        
        for i in range (len(nums)):
            if nums[nums[i] - 1] / len(nums) == 2 and nums[nums[i] - 1] % len(nums) == 0:
                ans.append(i)
        
        return ans

class leetcode1:
    def twoSum(nums: List[int], target: int) -> List[int]:
        # a dictionary of lists
        nums_set = {}
        for i in range (len(nums)):
            if nums[i] in nums_set:
                nums_set[nums[i]].append(i)
            else:
                nums_set.update({nums[i]: [i]})
        print(nums_set)
        
        # iter through nums - original list
        for i in range (len(nums)):
            complement = target - nums[i]
            # if the complement exists in hashtable 
            # AND
            # if it's not the same as nums[i]
            if nums_set[complement] != None:
                if complement != nums[i]:
                    return [i, nums_set[complement][0]]
                else:
                    if len(nums_set[complement]) == 2:
                        return nums_set[complement]
                
        return []


if __name__ == "__main__":
    # nums = [4,3,2,7,8,2,3,1]
    # nums = [2,7,11,15]
    nums = [2,5,5,11]

    #dup = leetcode442()
    #ans = dup.findDuplicates(nums)

    two_sum = leetcode1()
    #print(two_sum.twoSum(nums, 10))

    a, b, c, d = 1, 1, 1, 1

    print(a == b == c == d)


        