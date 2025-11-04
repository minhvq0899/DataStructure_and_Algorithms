"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================================ Stack ============================================================
(Monotonic stack implementation)
monotonicStack()
496, 503, 739, 901

    (Easy)
Leetcode 20. Valid Parentheses
    isValid_easy
    isValid_medium
Leetcode 1047. Remove All Adjacent Duplicates In String
Leetcode 1544. Make The String Great
Leetcode 496. Next Greater Element I - use Monotonic stack

    (Medium)
    "Medium - Parentheses related"
Leetcode 856. Score of Parentheses
Leetcode 2116. Check if a Parentheses String Can Be Valid (2 Stacks + Greedy)
Leetcode 1963. Minimum Number of Swaps to Make the String Balanced (Similar to 921 and 1541)
Leetcode 921. Minimum Add to Make Parentheses Valid

    "Medium - Monotonic stack"
Leetcode 739. Daily Temperatures - use Monotonic stack
Leetcode 503. Next Greater Element II  - use Monotonic stack
Leetcode 1762. Buildings With an Ocean View - Premium

    "Medium - Basic calculator series
Leetcode 227. Basic Calculator II
Leetcode 224. Basic Calculator
Leetcode 772. Basic Calculator III
Leetcode 150. Evaluate Reverse Polish Notation

    "Medium - basic stack"
Leetcode 443. String Compression
Leetcode 394. Decode String
Leetcode 1381. Design a Stack With Increment Operation
Leetcode 71. Simplify Path
Leetcode 735. Asteroid Collision

    (Hard)
    "Hard - Monotonic stack"
Leetcode 84. Largest Rectangle in Histogram - use Monotonic stack
Leetcode 85. Maximal Rectangle - use Monotonic stack
Leetcode 1944. Number of Visible People in a Queue - - use Monotonic stack

    (Implementation)
Leetcode 155. Min Stack
Leetcode 716. Max Stack - Premium

"""

from typing import List, Tuple
from collections import defaultdict, deque
import math
import heapq

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
    # Monotonic Stack
    # Used to solve NGE problems
    def monotonicStack(self, nums: List[int]):
        monotonicStack = []
        nge = [-1 for _ in range (len(nums))]
        
        for i in range (len(nums)-1, -1, -1):
            # Maintain the order
            while monotonicStack and monotonicStack[-1] <= nums[i]:
                monotonicStack.pop()

            # Find nge for NGE
            if len(monotonicStack) == 0:
                nge[i] = -1
            else:
                nge[i] = monotonicStack[-1]

            # Push the element into the stack as we know the order is maintained
            monotonicStack.append(nums[i])
        
        print(nge)
        return nge
                


    # ===========================================================================================
    # Leetcode 20
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

    # ===========================================================================================
    "Medium - Parentheses related"
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
    # Leetcode 2116. Check if a Parentheses String Can Be Valid
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        
        # Modify the input string
        modifiedS = ""
        for i in range (len(locked)):
            if locked[i] == "1":
                modifiedS += s[i]
            else:
                modifiedS += "x"

        print("modifiedS: ", modifiedS)
        
        # Two stacks
        stack_locked = []           # Contains locked opening paren
        stack_unlocked = []         # Contains unlocked char

        for i in range (len(modifiedS)):
            p = modifiedS[i]

            # Populate the stack
            if p == "(":
                stack_locked.append(i)
            elif p == "x":
                stack_unlocked.append(i)
            # If it's a locked closing parentheses, apply greedy logic always pop from locked stack first
            else:
                if stack_locked:
                    stack_locked.pop()
                elif stack_unlocked:
                    stack_unlocked.pop()
                else:
                    return False         

        print("stack_locked: ", stack_locked)
        print("stack_unlocked: ", stack_unlocked)

        # Handle the left-over in stack_locked
        while stack_locked:
            op_index = stack_locked.pop()
            if not stack_unlocked or stack_unlocked[-1] < op_index:
                return False
            stack_unlocked.pop()

        # Handle the left-over in stack_unlocked
        if stack_unlocked:
            if len(stack_unlocked) % 2 == 1: return False

        return True

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 1963. Minimum Number of Swaps to Make the String Balanced
    # When parsing the string:
    #   Every '[' increases balance.
    #   Every ']' decreases balance.
    # If balance ever goes negative, it means we’ve seen more closing brackets than opening ones — which is invalid at that point in the string. 
    # To fix this, we need to swap a future '[' to this position.
    # Each swap fixes two brackets:
    #   One misplaced ']'
    #   One '[' from later in the string
    # So if the maximum imbalance is k, we need k // 2 swaps to fix it. But since imbalance can be odd, we round up:
    # ---> ceil(k / 2) = (k + 1) // 2
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        maxImbalance = 0       

        # Iterate over the string and keep track of the number of opening and closing brackets on each step.
        for bracket in s:
            if bracket == "[":
                imbalance -= 1
            else:   # "]"
                imbalance += 1
            
            if imbalance > 0:
                maxImbalance = max(maxImbalance, imbalance)
        
        # print(maxImbalance)
        return (maxImbalance+1)//2

    
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 921. Minimum Add to Make Parentheses Valid
    def minAddToMakeValid(self, s: str) -> int:
        # number of closing parenthese that never saw an opening 
        redundant_closing = 0
        
        # This stack will only contain '('
        # Any valid substring will get processed by the stack 
        # What's left in the stack will be number of '(' that never closed
        stack = []      

        for p in s:
            if p == ')':
                if stack:
                    stack.pop()
                else:
                    redundant_closing += 1
            else:
                stack.append(p)

        return redundant_closing + len(stack)
                
        



    "Medium - Monotonic stack"
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 496. Next Greater Element I
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Compute the NGE for all elements in nums2
        stack = []                          # monotonic stack
        nge = [-1 for _ in range (len(nums2))]

        for i in range (len(nums2)-1, -1, -1):
            # Make sure the stack is in right order
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            # Compute the NGE for nums2[i]
            if stack:
                nge[i] = stack[-1]
            else:
                nge[i] = -1

            # Append nums2[i] to stack
            stack.append(nums2[i])

        print(nge)

        # Step 2: Store nums2 element and its NGE in a dict for fast look up later
        ngeDict = defaultdict(int)
        for i, num in enumerate(nums2):
            ngeDict[num] = nge[i]

        # Step 3: Prepare the nge list for nums1
        ngeNums1 = [-1 for _ in range (len(nums1))]
        for i, num in enumerate(nums1):
            ngeNums1[i] = ngeDict[num]

        return ngeNums1

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 739. Daily Temperatures
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # We will compute the NGE of each element in T
        stack = []      # monotonic stack that contains (temp, index)
        nge = [ 0 for _ in range (len(T)) ]
    
        for i in range (len(T)-1, -1, -1):
            tem = T[i]

            # Maintain the order of the stack
            while stack and stack[-1][0] <= tem:
                stack.pop()

            # Compute the NGE
            if stack:
                indexOfNGE = stack[-1][1]    
                days = indexOfNGE - i
                nge[i] = days
            # else: nge[i] = 0

            # Add tem to stack
            stack.append((tem, i))
        
        return nge

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 503. Next Greater Element II  - use Monotonic stack
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # we will iterate over the array two times to make it circular
        circularNums = nums + nums
        print(circularNums)

        # compute the nge for circularNums
        stack = []          # monotonic stack (largest at the bottom)
        ngeCircularNums = [-1 for _ in range (len(circularNums))]
        for i in range (len(circularNums)-1, -1, -1):
            # Maintain the order
            while stack and stack[-1] <= circularNums[i]:
                stack.pop()

            # Get the NGE for element i-th
            if stack:
                ngeCircularNums[i] = stack[-1]
            # else: nge[i] is already -1

            # Add element i-th to the stack
            stack.append(circularNums[i])

        # The NGE of i-th element in nums will be the same as the NGE of i-th element in circularNums
        ngeNums = [-1 for _ in range (len(nums))]
        for i in range (len(ngeNums)):
            ngeNums[i] = ngeCircularNums[i]

        return ngeNums

    # ----------------------------------------------------------------------------------------------------------------------------------------        
    # Leetcode 1762. Buildings With an Ocean View - Premium
    # We don’t need Monotonic Stack for this problem. We just need to scan one time from right to left and keep track of the tallest building seen so far.
    # Monotonic stack solution tells us which element (its index) is the NGE.
    # For this problem, we don’t need to know the exact NGE, just whether one exists.
    # Solution 1: Basic use of Monotonic stack
    def findBuildings(self, heights: List[int]) -> List[int]:
        # For this problem, this should be "next greater or equal element"
        # nge = [-1 for _ in range(len(heights))]
        stack = []
        result = []
        
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]

            # Step 1: Maintain the order of our monotonic stack
            while stack and heights[stack[-1]] < h:
                stack.pop()

            # Step 2: Compute the NGOEE for element at index i-th
            # if stack:
            #     nge[i] = stack[-1]

            # Optimization 
            if not stack:
                result.append(i)

            # Step 3: 
            stack.append(i)

        # print(nge)
        # result = [i for i in range(len(nge)) if nge[i] == -1]

        # print(result)
        result.reverse()
        return result

    # Solution 2: One pass Right -> Left
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        maxHeight = -1

        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            
            if h > maxHeight:
                result.append(i)
                maxHeight = h

        result.reverse()
        return result






    "Medium - basic stack"
    # Leetcode 443. String Compression
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


    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 735. Asteroid Collision
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Only collide if asteroid is going left and there's a right-moving one on top
            # Case 1: stack is empty 
            #   1.1. asteroid is left-flying -> simply add asteroid to stack (in the if statement below)
            #   1.2. asteroid is right-flying -> simply add asteroid to stack (in the if statement below)

            # Only start going into while loop if asteroid is left-flying and stack is non-empty
            while stack and asteroid < 0 and stack[-1] > 0:
                # Case 2: stack is not empty -> there might be collision
                top = stack[-1]
                
                # Case 2.1: left-flying wins
                if top < abs(asteroid):
                    # Right-moving asteroid explodes; keep checking
                    stack.pop()
                    continue
                # Case 2.2: Ties
                elif top == abs(asteroid):
                    # Both explode
                    stack.pop()
                    asteroid = 0  # mark current left-flying asteroid as destroyed
                    break
                # Case 2.3: right-flying wins
                else:
                    # Current asteroid destroyed
                    asteroid = 0
                    break

            # Add asteroid only if it survived all collisions
            if asteroid != 0:
                stack.append(asteroid)

        return stack
    
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 71. Simplify Path
    # Use the stack to mimic the behavior of directory management
    def simplifyPath(self, path: str) -> str:
        stack = []  # Stack to hold valid directory names

        # Split the path by '/' to isolate components
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                # Skip empty strings and '.' (current directory)
                continue
            elif part == '..':
                # '..' means go up one level — pop from stack if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name — push onto stack
                stack.append(part)

        # Join stack contents with '/' and prepend root slash
        return '/' + '/'.join(stack)


    # ----------------------------------------------------------------------------------------------------------------------------------------
    """ Basic Calculator series """
    # Leetcode 227. Basic Calculator II
    def calculate2(self, s: str) -> int:
        stack = []
        i = 0
        num = 0
        prev_op = '+'               # starts with '+' to handle the first number
        operators = {'+', '-', '*', '/'}

        # Process all '*' and '/'
        while i < len(s):
            char = s[i]

            # Scenario 1: char is a digit
            # here if char is ' ' then we simply just continue
            if char.isdigit():
                num = num*10 + int(char)

            # Scenario 2: char is an operator
            if char in operators or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append( int(stack.pop() / num) )

                # Reset
                prev_op = char
                num = 0

            i += 1

        return sum(stack)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 224. Basic Calculator
    """

    """
    def calculate1(self, s: str) -> int:
        # Evaluate expression s from index i
        # Stop when encouter ')'. Return result of the expression within () and ending index
        # ---------------------------------------------------------------
        def evaluate(s: str, i: int) -> Tuple[int, int]:
            stack = []
            operators = {'+', '-'}
            num = 0
            prev_op = '+'

            while i < len(s):
                char = s[i]

                # Scenario 1: Handle 'num'
                # char can be a digit or the start of new expression
                # here if char is ' ' then we simply just continue
                if char.isdigit():
                    num = num*10 + int(char)
                elif char == '(':
                    num, i = evaluate(s, i+1)
                    char = s[i] if i < len(s) else ')'

                # Scenario 2: Handle adding 'num' to our stack
                # char is an operand or end of an expression
                if char in operators or char == ')' or i == len(s) - 1:
                    if prev_op == '+':
                        stack.append(num)
                    elif prev_op == '-':
                        stack.append(-num)

                    # Reset
                    prev_op = char
                    num = 0

                # Scenario 3: End of an expression is a closing paren
                if char == ')':
                    return sum(stack), i+1
                
                i += 1

            # print(stack)
            return sum(stack), i
        # ---------------------------------------------------------------

        answer, _ = evaluate(s, 0)
        print(answer)
        return answer

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 772. Basic Calculator III
    def calculate(self, s: str) -> int:
        # Evaluate expression s from index i
        # Stop when encouter ')'. Return result of the expression within () and ending index
        # ---------------------------------------------------------------
        def evaluate(s: str, i: int) -> Tuple[int, int]:
            stack = []
            operators = {'+', '-', '/', '*'}
            num = 0
            prev_op = '+'

            while i < len(s):
                char = s[i]

                # Scenario 1: Handle 'num'
                # char can be a digit or the start of new expression
                # here if char is ' ' then we simply just continue
                if char.isdigit():
                    num = num*10 + int(char)
                elif char == '(':
                    num, i = evaluate(s, i+1)
                    char = s[i] if i < len(s) else ')'

                # Scenario 2: Handle adding 'num' to our stack
                # char is an operand or end of an expression
                if char in operators or char == ')' or i == len(s) - 1:
                    if prev_op == '+':
                        stack.append(num)
                    elif prev_op == '-':
                        stack.append(-num)
                    elif prev_op == '*':
                        stack.append(stack.pop() * num)
                    elif prev_op == '/':
                        stack.append(int(stack.pop() / num))
                    
                    # Reset
                    prev_op = char
                    num = 0

                # Scenario 3: End of an expression is a closing paren
                if char == ')':
                    return sum(stack), i+1
                
                i += 1

            # print(stack)
            return sum(stack), i
        # ---------------------------------------------------------------

        answer, _ = evaluate(s, 0)
        print(answer)
        return answer

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 150. Evaluate Reverse Polish Notation
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            # Case 1: char is a number (positive or negative)
            if char.isnumeric() or (char.startswith('-') and len(char) > 1 and char[1:].isnumeric()):
                stack.append(int(char))
            # Case 2: char is an operand
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                else:
                    # In Python, int() makes sure the division between two integers always truncates toward zero
                    stack.append(int(num1 / num2))
        
        return stack.pop()








    # ========================================================================================================================================
    "Hard"
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 84. Largest Rectangle in Histogram - use Monotonic stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        startingIndex_height_stack = []         # pair: (starting index, height)
        maxArea = 0

        for i, currentHeight in enumerate(heights):
            start = i
            # (1) Make sure the stack is in the right order
            # If height of startingIndex_height_stack[-1] > heights[i] --> Stop, compute maxArea, and pop the stack
            # Monotonic stack
            while startingIndex_height_stack and startingIndex_height_stack[-1][1] > currentHeight:
                startingIndex, height = startingIndex_height_stack.pop()
                maxArea = max(maxArea, (i-startingIndex)*height)
                start = startingIndex                   # reset the starting index for currentHeight 
            
            # (2) If height of startingIndex_height_stack[-1] <= heights[i] --> Found a new rec to track
            # Add current bar to the stack
            startingIndex_height_stack.append( (start, currentHeight) )

        # Compute the rec area of what's left in the stack
        for i, currentHeight in startingIndex_height_stack:
            maxArea = max(maxArea, currentHeight*(len(heights) - i))

        return maxArea


    # ----------------------------------------------------------------------------------------------------------------------------------------
    # matrix = [ ["1","0","1","0","0"],
    #            ["1","0","1","1","1"],
    #            ["1","1","1","1","1"],
    #            ["1","0","0","1","0"] ]
    # 
    # histograms = [ [1,0,1,0,0],
    #                [2,0,2,1,1],
    #                [3,1,3,2,2],
    #                [4,0,0,3,0] ]
    # Leetcode 85. Maximal Rectangle
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Step 1: Compute all mini histograms
        histograms = [[0 for _ in range (len(matrix[0]))] for _ in range (len(matrix))]

        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                # Case 0: First row
                if r == 0:
                    histograms[r][c] = int(matrix[r][c])
                # Case 1: matrix[r][c] == "0"
                elif matrix[r][c] == "0":
                    histograms[r][c] = 0
                # Case 2: matrix[r][c] == "1"
                else:
                    histograms[r][c] = histograms[r-1][c] + 1

        # print(histograms)

        # Step 2: Compute maxAre for each rec in each mini histograms
        maxArea = 0
        for histogram in histograms:
            maxArea = max(maxArea, self.largestRectangleArea(histogram))

        print("maxArea: ", maxArea)
        return maxArea


    # ----------------------------------------------------------------------------------------------------------------------------------------
    # Leetcode 1944. Number of Visible People in a Queue
    # In example 'heights' = [10,6,8,5,11,9], the reason why 0-th person cannot see 3-th person is because 
    # index 3th has already been popped by someone shorter than 0th person before
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Same idea as finding the NGE. This array contains indices instead of actual height
        # stack[0] will be the largest element
        monotonicStack = []

        # nge = [-1] * len(heights)
        # in this problem, instead of recording the nge, we record this info
        visible = [0]*len(heights)          

        for i in range(len(heights)-1, -1, -1):
            # The number of people we need to pop from the monotonic stack while maintaining 
            # the order is the number of people the i-th person can see to their right
            visibleCount = 0

            # Step 1: Maintain the order of the stack
            while monotonicStack and heights[monotonicStack[-1]] <= heights[i]:
                monotonicStack.pop()
                visibleCount += 1

            # Step 2: Compute the result
            # If the stack is not empty, then the # people the i-th person can see to their right will be visibleCount + 1 
            # (including the extra person in the stack)
            if monotonicStack:
                visible[i] = visibleCount + 1
            else:
                visible[i] = visibleCount
            
            # Step 3: Add the current height to the stack
            monotonicStack.append(i)

        return visible

            




""" Implementation """
# -----------------------------------------------------------------------------------------------------------
# Leetcode 155. Min Stack
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        currentMin = float('inf') if not self.stack else self.stack[-1][1]
        if val < currentMin:
            currentMin = val
        
        self.stack.append((val, currentMin))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        

# -----------------------------------------------------------------------------------------------------------
# Leetcode 716. Max Stack - Premium
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.alive = True  # Used for lazy deletion

class DoublyLinkedList:
    # In all operations, always keep 'head' and 'tail' as Node(0) to avoid null pointer
    def __init__(self):
        self.head = Node(0)  # Sentinel head
        self.tail = Node(0)  # Sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Add a node to the end of linked list
    def append(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    # Remove the last node
    def pop(self) -> Node:
        node = self.tail.prev
        self.remove(node)
        return node

    def peek(self) -> Node:
        return self.tail.prev

    # Remove a node from the linked list
    def remove(self, node):
        node.alive = False
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class MaxStack:
    # The heap will also contain the LinkedList node. 
    # This way we don't need a dict
    def __init__(self):
        self.dll = DoublyLinkedList()       # Acts as our stack
        self.heap = []                      # Max heap: (-val, timestamp, node)
        
        # Python integers are unbounded (int can grow arbitrarily large), so you won't hit overflow in Python itself.
        # But in other languages (like Java, C++, or Go), using a fixed-width integer (e.g., int32, int64) can overflow if the stack is used heavily over time.
        # Even in Python, using massive timestamps can slow down comparisons or heap operations due to memory pressure.
        # Alternative: use a defaultdict(list), where each value maps to a stack of node
        self.timestamp = 0

    def push(self, x: int) -> None:
        node = Node(x)
        self.dll.append(node)
        
        # O(logN)
        # By negating the timestamp, we make sure to satisfy this requirement
        # "If there is more than one maximum element, only remove the top-most one"
        heapq.heappush(self.heap, (-x, -self.timestamp, node))      
        self.timestamp += 1

    # O(1)
    def pop(self) -> int:
        node = self.dll.pop()
        node.alive = False
        return node.val

    # O(1)
    def top(self) -> int:
        return self.dll.peek().val

    # Worst case: O(NlogN)
    def peekMax(self) -> int:
        # First, pop all stale node from the heap
        while self.heap and not self.heap[0][2].alive:
            heapq.heappop(self.heap)

        return -self.heap[0][0]

    def popMax(self) -> int:
        # First, pop all stale node from the heap
        while self.heap and not self.heap[0][2].alive:
            heapq.heappop(self.heap)

        _, _, node = heapq.heappop(self.heap)
        self.dll.remove(node)
        return node.val








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
    # lc503 = [1,2,3,4,3]
    # lc84 = [1,0]
    # matrix85 = [ ["1","0","1","0","0"],
    #            ["1","0","1","1","1"],
    #            ["1","1","1","1","1"],
    #            ["1","0","0","1","0"] ]

    # -----------------------------------------------------------
    leetcode = Solution()

    # leetcode.monotonicStack(lc496_nums2)

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

    # ----------------------- 2116. Check if a Parentheses String Can Be Valid -----------------------
    # s = "(((())(((())"
    # locked = "111111010111"
    # print(leetcode.canBeValid(s, locked))

    # ----------------------- 1963. Minimum Number of Swaps to Make the String Balanced -----------------------
    # s = "[[[]]]][][]][[]]][[["      # expect 2
    # ans1963 = leetcode.minSwaps(s)
    # print("ans1963: ", ans1963)

    # print(leetcode.nextGreaterElement(lc496_nums1, lc496_nums2))

    # ----------------------- 1944 -----------------------
    # heights = [10,6,8,5,11,9]
    # print(leetcode.canSeePersonsCount(heights))

    # daily_temp = leetcode.dailyTemperatures(lc739)
    # print(daily_temp)

    # print("Score of this parentheses is ", leetcode.scoreOfParentheses(lc856))

    # nge_medium = leetcode.nextGreaterElements(lc503)
    # print(nge_medium)

    # ----------------------- 84 + 85 -----------------------
    # answer84 = leetcode.largestRectangleArea(lc84)
    # print(answer84)
    # answer85 = leetcode.maximalRectangle(matrix85)

    # ----------------------- 71 -----------------------
    # path = "/a/./b/../../c/"
    # leetcode.simplifyPath(path)

    # ----------------------- 227 -----------------------
    s = "2*(5+5*2)/3+(6/2+8)"
    leetcode.calculate(s)

    # ----------------------- 150 -----------------------
    # tokens = ["3","-4","+"]
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # print(leetcode.evalRPN(tokens))

    # ----------------------- 1762 -----------------------    
    # heights = [7,5,3,2,6,9,3,2]
    # leetcode.findBuildings(heights)





