"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================================ Stack ============================================================

Leetcode 20. Valid Parentheses
    isValid_easy
    isValid_medium
Leetcode 1047. Remove All Adjacent Duplicates In String
Leetcode 443. String Compression
Leetcode 394. Decode String
Leetcode 1544. Make The String Great
Leetcode 739. Daily Temperatures
Leetcode 496. Next Greater Element I
Leetcode 856. Score of Parentheses
Leetcode 1381. Design a Stack With Increment Operation

(Hard)
Leetcode 224. Basic Calculator


"""

from typing import List

# ----------------------------------------------------------------------------------------------------------------------------------------
# Leetcode 1381. Design a Stack With Increment Operation
class Entry:
    def __init__(self, value: int, offset: int):
        self.val = value
        self.offset = offset

class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = list()
        self.cap = maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.cap:
            self.stack.append( Entry(x, 0) )
            self.size += 1
            
    def pop(self) -> int:
        top = self.stack.pop()
        self.size -= 1
        if self.size != 0:
            self.stack[-1].offset += top.offset

        return top.val + top.offset
        
    def increment(self, k: int, val: int) -> None:
        k = min(k, self.size)
        self.stack[k-1].offset += val


class Solution:
    # --------------------------------------------------------------------------------------------
    # Leetcode 20
    # first just take it easy
    # s only contains "(" and ")"
    def isValid_easy(self, s: str) -> bool:
        stack = []
        for para in s:
            if para == '(':
                stack.append(para)
            else:
                if not stack: # True if list is empty
                    return False
                else: 
                    stack.pop()

        return not stack # if by the end, stack is empty then s is valid

    # this time, s can contain '(', ')', '{', '}', '[', ']'
    def isValid_medium(self, s: str) -> bool:
        # prepare a dictionary
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for para in s:
            if para not in mapping: # meaning it's one of the opening brackets
                stack.append(para)
            else: # for closing brackets
                if not stack: # stack is empty
                    return False
                else: 
                    pop = stack.pop()
                    if mapping.get(para) != pop: 
                        return False
        
        return not stack

    # --------------------------------------------------------------------------------------------
    # Leetcode 1047
    def removeDuplicates(self, S: str) -> str:
        pass

    # --------------------------------------------------------------------------------------------
    # Leetcode 443
    def compress(self, chars: List[str]) -> int:
        stack = []
        for char in chars:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                item = stack.pop()
                item[1] += 1
                stack.append(item)
        
        chars.clear()
        
        for item in stack:
            # append the character
            chars.append(item[0])

            # append the frequency
            if item[1] != 1: 
                freq_str = str(item[1]) 
                for i in range (len(freq_str)):
                    chars.append(freq_str[i])

        return len(chars)

    # --------------------------------------------------------------------------------------------
    # Leetcode 394
    def decodeString(self, s: str) -> str:
        integers_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        main_stack = [] # main stack to use

        # iter through each char in s
        for i in range (len(s)):
            # keep append until we see a "]"
            if s[i] != ']':
                main_stack.append(s[i])
            else: # we see a closing bracket
                temp_stack = []
                looking_for_opening_brac = True
                # pop main strack until we see a "["
                while looking_for_opening_brac:
                    item = main_stack.pop()
                    if item == '[': 
                        looking_for_opening_brac = False
                    else:
                        temp_stack.append(item)

                # before a "[" must be an integer
                int_stack = []
                looking_for_int = True
                while looking_for_int and len(main_stack) != 0: 
                    possible_int = main_stack.pop()
                    if possible_int in integers_set: # O(1)
                        int_stack.append(possible_int)
                    else: # oops we pop one too many
                        looking_for_int = False
                        main_stack.append(possible_int)

                # convert our str into int
                freq = int("".join(reversed(int_stack)))
                # now append those item in temp_stack back into main_stack for freq times
                for k in range(freq):
                    for v in reversed(range(len(temp_stack))):
                        main_stack.append(temp_stack[v])
            
        return "".join(main_stack)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 1544. Make The String Great
    def makeGood(self, s: str) -> str:
        stack = []
        
        # we only check the previous char to avoid possible index out of bound
        for i in range(len(s)):
            if not stack: # if stack is empty
                stack.append(s[i])
            # if the previous is NOT the uppercase/ lowercase version
            elif ord(s[i]) != ord(stack[-1])+32 and ord(s[i]) != ord(stack[-1])-32:
                stack.append(s[i])
            else: # if it is, then pop
                stack.pop()

        return "".join(stack)

        """
        i = 0
        s_final = ''

        while s_final != s: 
            while i < len(s):
                # if the char is uppercase
                if 64 < ord(s[i]) < 91:
                    # check previous char 
                    prev = stack.pop() if i != 0 else ' ' # aware of the possible out of range index if i == 0
                    print(prev)
                    if ord(prev) - 32 == ord(s[i]): # if previous char is the lowercase of s[i]
                        i += 1
                    elif i <= len(s) - 2 ord(s[i]) + 32 == ord(s[i+1]): # check following char
                        if prev != ' ': stack.append(prev)
                        i += 2  
                    else: # if it's an uppercase but there isn't any lowercase infront or behind it then append that uppercase into stack
                        if prev != ' ': stack.append(prev)
                        stack.append(s[i])
                        i += 1
                else: # if the char is lowercase
                    stack.append(s[i])
                    i += 1
            
                print(stack)
            
            s = "".join(stack)

        return s_final
        """

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 496. Next Greater Element I
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # we will find the NGE of all elements in nums 2 and store them into this dict
        mapping = {}
        # this stack will be sorted: largest will be in the bottom
        stack = []
        # first append the first element of nums2 into stack
        stack.append(nums2[0]) 

        # iteration
        for i in range (1, len(nums2)):
            pop = stack.pop()
            # compare the current element each element in stack until find the larger element
            while nums2[i] > pop: 
                mapping.update({pop: nums2[i]})
                if not stack: break 
                else: pop = stack.pop()

            if pop > nums2[i]: 
                stack.append(pop)

            stack.append(nums2[i])     

        # the NGEs for all elements left in the stack is -1
        for item in stack:
            mapping.update({item: -1})       

        # return only NGE of elements in nums1
        for i in range (len(nums1)):
            nums1[i] = mapping.get(nums1[i])

        return nums1 

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 739. Daily Temperatures
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = []
        stack = []
        stack.append([T[0], 0])

        for i in range (1, len(T)):
            prev = stack.pop()
            if T[i] <= prev[0]: 
                stack.append(prev)
            else:
                while T[i] > prev[0]:    
                    ans[prev[1]] = i - prev[1]
                    if not stack: break
                    else: prev = stack.pop() 
            # always finish with appending the current element into the stack
            stack.append([T[i], i])
        
        # for elements left in the stack, they have no NGE
        for item in stack:
            ans[item[1]] = 0

        return ans

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 856. Score of Parentheses
    def scoreOfParentheses(self, S: str) -> int:
        depth_score = [0] # depth 0 (has value 0) is for when the last time we pop

        for c in S:
            if c == "(": # just keep adding depth
                depth_score.append(0)
            else: 
                prev = depth_score.pop()
                depth_score[-1] += max(2*prev, 1) # it's either a () or (A)

        return depth_score[0]

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 503. Next Greater Element II  - use Monotonic stack
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # we will iterate over the array two times to make it circular
        stack = []
        res = [-1] * len(nums)
        for i in reversed(range(2*len(nums))):
            index_nums = i % len(nums)
            # our stack will have this order: largest at the bottom, 
            # smaller on top (peek)
            while len(stack) != 0 and stack[-1][0] <= nums[index_nums]:
                stack.pop()
            
            if len(stack) != 0: res[index_nums] = stack[-1][0] # this is stack peek

            stack.append([nums[index_nums], index_nums])
        
            print(stack)

        return res


    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 224. Basic Calculator
    """
    - Stack keeps track of the sign context introduced by parentheses.
    - When you see a (, you push the current sign.
    - When you see a ), you pop the sign context.
    - Numbers are built digit by digit and added to the result with the correct sign.
    """











# =================================================================================================================================================
# =================================================================================================================================================















if __name__ == "__main__":
    # s = '()()(())'
    # s = '{[{}]()}'
    # lc443 = ["a"]
    # lc394 = "100[leetcode]"
    # lc1544 = "ABbcCa"
    # lc496_nums2 = [1,3,4,2] 
    # lc496_nums1 = [4,1,2]
    # lc739 = [73,74,75,71,69,72,76,73]
    # lc856 = "(()(()))"
    lc503 = [1,2,3,4,3]

    # -----------------------------------------------------------
    leetcode = Solution()
    #easy = isValid.isValid_easy(s) 
    #print('Easy: ', easy)

    # med = isValid.isValid_medium(s)
    # print('Medium: ', med)

    # cpr = isValid.compress(lc443)
    # print('Compress: ', cpr)

    # decoded = leetcode.decodeString(lc394)
    # print(decoded)

    # goodstr = leetcode.makeGood(lc1544)
    # print(goodstr)

    # print(leetcode.nextGreaterElement(lc496_nums1, lc496_nums2))

    # daily_temp = leetcode.dailyTemperatures(lc739)
    # print(daily_temp)

    # print("Score of this parentheses is ", leetcode.scoreOfParentheses(lc856))

    nge_medium = leetcode.nextGreaterElements(lc503)
    print(nge_medium)












