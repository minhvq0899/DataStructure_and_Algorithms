"""
Meta screening technical interview

Question 1: We have this View class as defined below
Given a target 'view' and a list of view, return all the views in that list that are parent of view

Question 2: Implement the Candy Crush logic
    Eg. Input: “abbba”  --->  Output: empty str
Leetcode 1047: Remove All Adjacent Duplicates In String (Easy)
Follow-up: Leetcode 1209 - Remove All Adjacent Duplicates in String II (Medium)

"""

from typing import List, Optional
from collections import defaultdict


"""
Question 1
"""
class View:
    # Here is has to be "View" instead of View because of Forward Reference
    # Python evaluates type hints at runtime unless you delay them
    # By putting "View" in quotes, you're telling Python: “This refers to a class that will be defined later"
    def __init__(self, name: str, subViews: Optional[List["View"]] = None):
        self.name = name
        self.subViews = subViews if subViews != None else []

    def hasSubView(self, view: "View") -> bool:
        for v in self.subViews:
            if view.name == v.name:
                return True
            
        return False


# Given a 'targetedView' and a list of views, return all the views in that list that are parent of targetedView
def parents(targetedView: View, views: List[View]) -> List[str]:
    cache = {}          # Key: a pair of isDescendant() parameters (parent name, target name) -> Value: a bool representing if 'target' is a descendant of 'parent'
    # -----------------------
    # Given a 'parent' view and 'target' view, return True if 'target' is descendant of 'parent'
    def isDescendant(parent: View, target: View) -> bool:
        # Base case 1: reach an already computed subtree
        if (parent.name, target.name) in cache:
            return cache[(parent.name, target.name)]
        # Base case 2: reach the leave view
        if parent == target:
            return True
        
        # Recursive part
        for sub in parent.subViews:
            if isDescendant(sub, target):
                cache[(parent.name, target.name)] = True
                return True

        cache[(parent.name, target.name)] = False
        return False
    # -----------------------

    result = []
    for view in views:
        if isDescendant(view, targetedView):
            result.append(view.name)

    return result


a = View("A")
b = View("B")
c = View("C", [a])
d = View("D", [b, c])

# Notice: even though this 'a' is parent of its own, it's not included in 'ans' because our algorithm only checks
# each view in 'views' list. If 'a' is included in the 'views' list then ans will include 'a'
ans = parents(a, [b, c, d]) # → [c, d]
# print(ans)



"""
Question 2: Leetcode 1047 - Remove All Adjacent Duplicates In String (Easy)

Follow-up: Leetcode 1209 - Remove All Adjacent Duplicates in String II (Medium)
"""
class Solution:
    # Leetcode 1047 - Remove All Adjacent Duplicates In String
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for c in S:
            # Case 1: stack is empty
            if not stack: 
                stack.append(c)
            # Case 2: stack is not empty
            else: 
                # if the last item != c
                if stack[-1] != c:
                    stack.append(c)
                else:
                    stack.pop()
        
        return "".join(stack)


    # Leetcode 1209 - Remove All Adjacent Duplicates in String II (Medium)
    # The stack holds [char, count] pairs.
    # When a group count reaches EXACTLY k, it’s removed.
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []      # stores [char, count]

        for c in s:
            # Add new char
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            # Try to pop
            if stack[-1][1] == k: 
                stack.pop()

        # Reconstructing string
        s_list = []
        for char, count in stack:
            for _ in range(count):
                s_list.append(char)

        s = ''.join(s_list)

        return s
            

        














if __name__ == "__main__":
    leetcode = Solution()

    # s = "abbba"
    # print(leetcode.removeDuplicates(s))

    s = "deeedbbcccbdaa"
    print(leetcode.removeDuplicates(s, 3))