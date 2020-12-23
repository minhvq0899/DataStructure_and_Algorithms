"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Stack ==============================================

1. Leetcode 20. Valid Parentheses
    isValid_easy
    isValid_medium
2. Leetcode 1047. Remove All Adjacent Duplicates In String
3. Leetcode 443. String Compression
4. Leetcode 394. Decode String

"""

from typing import List

class Solution:
    # --------------------------------------------------------------------------------------------
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



if __name__ == "__main__":
    # s = '()()(())'
    # s = '{[{}]()}'
    # lc443 = ["a"]
    lc394 = "100[leetcode]"

    # -----------------------------------------------------------
    isValid = Solution()
    #easy = isValid.isValid_easy(s) 
    #print('Easy: ', easy)

    # med = isValid.isValid_medium(s)
    # print('Medium: ', med)

    # cpr = isValid.compress(lc443)
    # print('Compress: ', cpr)

    decoded = isValid.decodeString(lc394)
    print(decoded)





