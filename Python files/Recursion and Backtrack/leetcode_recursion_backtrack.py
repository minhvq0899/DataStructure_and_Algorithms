"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= DFS with template =========================================================
DFS down different path: 
    Leetcode 22. Generate Parentheses
    Leetcode 17. Letter Combinations of a Phone Number
    Leetcode 752. Open the Lock
    Leetcode 797. All Paths From Source to Target
    Leetcode 93. Restore IP Addresses - Backtracking
    Combination and Permutation series
        Leetcode 46. Permutation
        Leetcode 47. Permutation II
        Leetcode 267. Palindrome Permutation II
        Leetcode 39. Combination Sum
        Leetcode 40. Combination Sum II
        Leetcode 216. Combination Sum III
        Leetcode 377. Combination Sum IV
        Leetcode 77. Combinations
        Leetcode 78. Subsets
    Leetcode 1306. Jump Game III

DFS on grid/ matrix
    Leetcode 200. Number of Islands
        DFS solution
        BFS solution - recommended for interview, showcasing your knowledge about memory usage difference between DFS and BFS
    Leetcode 1254. Number of Closed Islands
    Leetcode 695. Max Area of Island
    Leetcode 827. Making A Large Island (Hard - very similar to 695)
    Leetcode 130. Surrounded Regions
    Leetcode 417. Pacific Atlantic Water Flow
    Leetcode 1020. Number of Enclaves
    Leetcode 529. Minesweeper
    Leetcode 934. Shortest Bridge ??
    Leetcode 1219. Path with Maximum Gold
    Leetcode 2664. The Knight’s Tour
    Leetcode 79. Word Search
    Leetcode 212. Word Search II - Hard
    Leetcode 36. Valid Sudoku
    Leetcode 37. Sudoku Solver
    Leetcode 51. N-Queens - follow up of Leetcode 52 - Hard
    Leetcode 52. N-Queens II - Hard
    
"""

import queue
from typing import List, Tuple 
from collections import Counter, defaultdict, deque
from math import factorial

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Solution:
    # Helper print function
    def printMatrix(self, grid):
        for row in grid:
            print(row)
    
    # -----------------------------------------------------------------------------------------------
    # Leetcode 22. Generate Parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        self.dfs_paren(n, "", 0, 0, combinations)

        return combinations

    def dfs_paren(self, n: int, potential: str, left: int, right: int, combinations: List[str]):
        # base case
        if len(potential) == 2*n:
            combinations.append( potential )
            return
        
        # variation
        if left < n:
            self.dfs_paren(n, potential + "(", left+1, right, combinations)
        if right < left:
            self.dfs_paren(n, potential + ")", left, right+1, combinations)
        
    
    # -----------------------------------------------------------------------------------------------
    # Leetcode 17. Letter Combinations of a Phone Number
    def letterCombinations(self, digits: str) -> List[str]:
        # create a data strucutre to store answers
        ans = []

        if digits != None and len(digits) > 0:
            mapping = ["", "", "abc", "def", "ghi", "jkl","mno","pqrs","tuv","wxyz"]
            d = digits[0] # if digits == "23" then d == "2"
            letters = mapping[ int(d) ] # letters == "abc"
            for char in letters:     
                self.dfs(digits, mapping, ans, 1, char)
            
        return ans

    def dfs(self, digits: str, mapping: List[str], ans: List[str], index: int, potential: str):
        # base cases: we found 1 combination
        if len(potential) == len(digits):
            ans.append(potential)
            return 
            
        # variation
        d = digits[index] # d == 2
        letters = mapping[ int(d) ]
        for char in letters:
            self.dfs(digits, mapping, ans, index + 1, potential + char)


    # ------------------------------------------------------------------------------------------
    # Leetcode 752. Open the Lock
    def openLock(self, deadends: List[str], target: str) -> int:
        # if each time you checks for deadends, you have to iterates through a list, it will be O(n)
        # instead, store you deadends in a set
        deadendsSet = {deadend for deadend in deadends}

        # initialize BFS
        q = queue.Queue()
        visited = [False for _ in range (10000)]
        path = [-1 for _ in range (10000)]

        # BFS
        visited[0] = True # we start at "0000"
        q.put("0000")

        while q.qsize() > 0:
            u = q.get()
            if u not in deadendsSet:
                neighbors = self.find_neighbor(u) # neighbors is a list
                for neighbor in neighbors:
                    neighbor_int = int(neighbor)
                    if not visited[neighbor_int]:
                        visited[neighbor_int] = True
                        path[neighbor_int] = int(u)
                        q.put( neighbor )

        # return 
        if target == "0000" and target not in deadendsSet:
            return 0
            
        count = 0
        target_int = int(target)
        if path[ target_int ] != -1:
            while target_int != 0:
                target_int = path[target_int]
                count += 1
            return count

        return -1
        # V là số đỉnh -> có 10000 đỉnh, tương ứng với 10000 trường hợp từ 0000 -> 9999
        # E là số đỉnh -> có 80000 cạnh, mỗi đỉnh trung bình có 8 cạnh (trừ các đỉnh deadends)
        # Time Complexity: O(10000 + 80000)
        # Extra Space Complexity: O(10000)
                
    # u passed into this find_neighbor is definitely not in deadends
    def find_neighbor(self, current: str) -> List[str]:
        neighbors_list = []
        current = list(current)

        for i in range (len(current)):
            digit = int( current[i] )    
            if digit == 9:
                # go up
                current[i] = "0"
                neighbors_list.append( "".join(current) )
                # go down
                current[i] = "8"
                neighbors_list.append( "".join(current) )
                # restore
                current[i] = "9"
            elif digit == 0:
                # go up 
                current[i] = "1"
                neighbors_list.append( "".join(current) )
                # go down
                current[i] = "9"
                neighbors_list.append( "".join(current) )
                # restore
                current[i] = "0"
            else: 
                # go up
                current[i] = str( digit + 1 )
                neighbors_list.append( "".join(current) )
                # go down
                current[i] = str( digit - 1 )
                neighbors_list.append( "".join(current) )
                # restore
                current[i] = str(digit)

        return neighbors_list
    
    def openLock_2025(self, deadends: List[str], target: str) -> int:
        if target == "0000": return 0
        deadend_set = set(deadends)
        if "0000" in deadend_set: return -1

        # paths will act as both Visited set and Path dict
        paths = collections.defaultdict(str)
        paths["0000"] = None
        q = queue.Queue()
        q.put("0000")

        while not q.empty():
            u = q.get()
            if u not in deadend_set:
                neighbors = self.find_neighbor(u)
                for neighbor in neighbors:
                    if neighbor not in paths and neighbor not in deadend_set:
                        paths[neighbor] = u
                        q.put(neighbor)
        
        for key,value in paths.items():
            print ("{}: {} \n".format(key,value) )

        answer = 0
        if target in paths:
            while target != "0000":
                target = paths[target]
                answer += 1
            return answer

        return -1


    # ------------------------------------------------------------------------------------------
    # Leetcode 797. All Paths From Source to Target
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []     # Stores all valid paths from source to target
        path = [0]      # Current path being explored (starts at node 0)
        # --------------------------------
        def dfs(node: int):
            # Base case: if we reach the target node (last node)
            if node == len(graph) - 1:
                result.append(list(path))  # Make a copy of the current path
                return

            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                path.append(neighbor)      # Choose: add neighbor to path
                dfs(neighbor)              # Explore: recurse from neighbor
                path.pop()                 # Un-choose: backtrack
        # --------------------------------
        # Start DFS from node 0
        dfs(0)
        return result
    

    # ------------------------------------------------------------------------------------------
    # Leetcode 93. Restore IP Addresses - Backtracking
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        if len(s) > 12: return results

        # -----------------------------------------
        def placeDot(index: int, numOfDots: int, curIP: str):
            # Base cases:
            if numOfDots == 4 and index == len(s):
                results.append(curIP[:-1])
                return
            if numOfDots > 4: 
                return
            
            # Action
            for j in range (index, min(index+3, len(s))):
                nextSegment = s[index:j+1]

                if isValidSegment(nextSegment):
                    # curIP += (nextSegment + ".")
                    placeDot(j+1, numOfDots+1, curIP + nextSegment + ".")

                # No need for explicit backtracking part here, because we are constructing the nextSegment for each dfs call

        def isValidSegment(segment: str) -> bool:
            if len(segment) == 1: return True
            if int(segment) < 256 and segment[0] != "0":
                return True
            
            return False
        # -----------------------------------------
        placeDot(0, 0, "")

        # print(results)
        return results


    """ Combination and Permutation series """
    # ------------------------------------------------------------------------------------------
    # Leetcode 46. Permutation
    def permute(self, nums: List[int]) -> List[List[int]]:
        permSet = set()
        used = [False] * len(nums)
        # ----------------------------------------------------------------------------
        def dfs(potential: List[int]):
            # base case 1 
            if len(potential) == len(nums):
                permSet.add(tuple(potential))
                return

            # todo: try each unused number
            for i in range (len(nums)):
                if used[i]:
                    continue
                
                # choose num[i]
                used[i] = True
                potential.append(nums[i])

                # explore further
                dfs(potential)

                # backtrack
                potential.pop()
                used[i] = False
        # ----------------------------------------------------------------------------
        dfs([])
        
        return list(list(perm) for perm in permSet)
    
    """
    This can be solved with the exact same solution as LC 46. Permutation because in that solution we used a Set to store solution. 
    However, without the additional pruning logic to avoid re-exploring the dup path, the solution will just take much more time 
    """
    # Leetcode 47. Permutation II
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permSet = list()
        used = [False] * len(nums)
        # ----------------------------------------------------------------------------
        def dfs(potential: List[int]):
            # base case 1 
            if len(potential) == len(nums):
                permSet.append(list(potential))
                return

            # todo: try each unused number
            for i in range (len(nums)):
                # if i-th num is already used, skip no question asked
                if used[i]:
                    continue
                # if i-th num is a dup AND the previous num (same value) not used
                if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                    continue
                
                # choose num[i]
                used[i] = True
                potential.append(nums[i])

                # explore further
                dfs(potential)

                # backtrack
                potential.pop()
                used[i] = False
        # ----------------------------------------------------------------------------
        dfs([])
        
        return permSet

    # Leetcode 267. Palindrome Permutation II
    def perm(self, charList: List[str]) -> List[List[str]]:
        answer = set()
        visited = [False] * len(charList)

        def dfs(potential: List[str]):
            # base cases:
            if len(potential) == len(charList):
                answer.add(tuple(potential))
                return

            # visit each unvisited char
            for i in range (len(charList)):
                if visited[i]:
                    continue
                
                # todo
                visited[i] = True
                potential.append(charList[i])

                # dfs
                dfs(potential)

                # backtrack
                visited[i] = False
                potential.pop()

        dfs([])

        return list( list(p) for p in answer )

    def generatePalindromes(self, s: str) -> List[str]:
        counterS = Counter(s)

        # do simple math to check if a permutation of s can be palindromic
        numOfOddCountChar = 0
        oddCountChar = ""
        charList = []
        for char, count in counterS.items():
            if count % 2 == 1:
                numOfOddCountChar += 1
                oddCountChar = char
            else:
                for _ in range (int(count/2)):
                    charList.append(char)

        # corner case
        if len(counterS) == 1: return [s]
        # permutation of s cannot form a palindrome
        if numOfOddCountChar > 1: 
            return []
        # in case the char with odd frequency has freq more than 1 (3,5,7,etc)
        if oddCountChar != "":
            countOddChar = counterS[oddCountChar]
            if countOddChar > 1:
                for _ in range (int((countOddChar-1)/2)):
                    charList.append(oddCountChar)

        # generate all unique permutations of charList
        permList = self.perm(charList)
        answer = []

        # add firstHalf + reverse(firsHalf)
        for halfString in permList:
            reverseHalfString = halfString[::-1]
            # if there is one char with odd freq, insert that char in the middle of two half
            if oddCountChar != "":
                palindromePerm = halfString + [oddCountChar] + reverseHalfString
                palindromePerm = "".join(palindromePerm)
                answer.append(palindromePerm)
            # else just simply merge two halves together
            else:
                palindromePerm = halfString + reverseHalfString
                palindromePerm = "".join(palindromePerm)
                answer.append(palindromePerm)

        return answer


        
    # ------------------------------------------------------------------------------------------
    # Leetcode 39. Combination Sum
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # ------------------------------------------------------------------------------
        def subsetCount(tar, potential, curIdx):
            # base case 1: found a combination
            if tar == 0: 
                ans.append(list(potential))
                return
            # base case 2: index out of bound
            if curIdx not in range (len(candidates)):
                return 
            # base case 3: target < 0
            if tar < 0:
                return 

            # recursive part
            # use that current index
            subsetCount(tar-candidates[curIdx], potential + [candidates[curIdx]], curIdx)
            # potential.pop()     # other solution will use this to backtrack
            # not use that current index <------ but we already backtrack with this
            subsetCount(tar, potential, curIdx + 1)
            
        # ------------------------------------------------------------------------------
        poten = list()
        subsetCount(target, poten, 0)
        return ans

    def combinationSum_backtrack(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # ------------------------------------------------------------------------------
        def dfs(tar, potential, start):
            # base case 1: found a combination
            if tar == 0: 
                ans.append(list(potential))
                return
            # base case 2: target < 0
            if tar < 0:
                return 

            for i in range (start, len(candidates)):
                potential.append(candidates[i])
                # recursive call
                dfs(tar-candidates[i], potential, i)
                # back track
                potential.pop()
        # ------------------------------------------------------------------------------
        dfs(target, [], 0)
        return ans

    def tripletSum_backtrack(self, candidates: List[int], divisor: int) -> int:
        seenTriplet = set()
        # cnt = 0

        # ------------------------------------------------------------------------------
        def dfs(potential, start):
            # nonlocal cnt
            # base case 2
            if len(potential) > 3:
                return 
            
            # base case 1: found a triplet
            if len(potential) == 3 and sum(potential) % divisor == 0: 
                seenTriplet.add( tuple(sorted(potential)) )
                # cnt += 1
                print(seenTriplet)
                print(cnt)
                return
            

            for i in range (start, len(candidates)):
                potential.append(candidates[i])
                # recursive call
                dfs(potential, i+1)
                # back track
                potential.pop()
        # ------------------------------------------------------------------------------
        dfs([], 0)

        return len(seenTriplet)


    # ------------------------------------------------------------------------------------------
    # Leetcode 40. Combination Sum II
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        # Step 1: DS to store answer
        answer = list()
        # --------------------------------------------------------------------------
        def dfs(poten, s, tar):
            # Base cases:
            if tar == 0:
                answer.append(list(poten))
                return 
            if tar < 0: return 
            
            # dfs
            for i in range (s, len(candidates)):
                # Skip duplicate. If i > s, it means you’ve moved beyond the first candidate considered at this level
                # Just think of this as pruning a whole dup tree path before it even starts because it has already been computed before
                if i > s and candidates[i] == candidates[i-1]: 
                    continue
                # try a candidate
                poten.append( candidates[i] )
                # dfs
                dfs(poten, i+1, tar-candidates[i])
                # backtrack
                poten.pop() 
                
        # --------------------------------------------------------------------------
        # Step 2: Do DFS/ BFS
        dfs([], 0, target)

        # Step 3:
        return answer

    # ------------------------------------------------------------------------------------------
    # Leetcode 216. Combination Sum III
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Step 1: DS to store answer
        answer = list()
        # --------------------------------------------------------------------------------------------------
        def dfs(poten, s, tar):
            # Base case:
            if tar == 0 and len(poten) == k:
                answer.append(list(poten))
                return 
            if not tar > 0: return 
            
            # dfs
            for i in range (s, 10):
                poten.append( i )
                dfs(poten, i+1, tar-i)
                poten.pop() # backtrack
                
        # --------------------------------------------------------------------------------------------------
        # Step 2: Do DFS/ BFS
        potential = list()
        dfs(potential, 1, n)

        # Step 3:
        return answer 

    # ------------------------------------------------------------------------------------------
    # Leetcode 377. Combination Sum IV
    # Currently this solution is running into TLE. Current idea is follow Leetcode39 above, and once we have all the combination, we compute the # of permutation from each combination
    # Instead of computing in the end, just make sure to add the Counter to ans instead of the list(potential)
    def count_permutations(self, counter: Counter) -> int:
        total_chars = sum(counter.values())  # Total characters
        denominator = 1
        
        for freq in counter.values():
            denominator *= factorial(freq)  # Multiply factorials of frequencies

        return factorial(total_chars) // denominator  # Apply formula

    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = []
        # ------------------------------------------------------------------------------
        def subsetCount(tar, potential, start):
            # base case 1: found a combination
            if tar == 0: 
                ans.append(list(potential))
                return
            # base case 2: target < 0
            if tar < 0:
                return 

            for i in range (start, len(nums)):
                potential.append(nums[i])
                # recursive call
                subsetCount(tar-nums[i], potential, i)
                # back track
                potential.pop()
        # ------------------------------------------------------------------------------
        subsetCount(target, [], 0)
        counter_frozensets = set()
        for answer in ans:
            c = Counter(answer)
            counter_frozensets.add(frozenset(c.items()))

        print(counter_frozensets)
        counter_sets = [Counter(dict(fset)) for fset in counter_frozensets]
        total_perm = 0
        for c in counter_sets:
            total_perm += self.count_permutations(c)

        return total_perm


    # ----------------------------------------------------------------------------------
    # Leetcode 78. Subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs78(nums, 0, [], result)

        print(result)
        return result

    def dfs78(self, nums: List[int], index: int, potential: List[int], result: List[List[int]]):
        # Base case
        if index == len(nums):
            result.append(potential.copy())
            return
        
        # Not include
        self.dfs78(nums, index+1, potential, result)

        # Include
        potential.append(nums[index])
        self.dfs78(nums, index+1, potential, result)
        potential.pop()

    
    # ------------------------------------------------------------------------
    # Leetcode 1306. Jump Game III
    def canReach(self, arr: List[int], start: int) -> bool:
        reach = []
        
        self.dfs_canReach(arr, start, reach)
        
        return True if reach else False
    
    def dfs_canReach(self, arr: List[int], index: int, reach: List[int]):
        # base cases
        if index < 0 or index >= len(arr):
            return 
        if arr[index] == 0:
            reach.append(1)
            return 
        if arr[index] < 0: 
            return 
        
        # TO DO
        arr[index] *= -1
        
        # call DFS where needed
        self.dfs_canReach(arr, index+arr[index], reach)
        self.dfs_canReach(arr, index-arr[index], reach)
















    # ================================================================================================================================================================================================================================================================================== 
    # ================================================================================================================================================================================================================================================================================== 
    # Leetcode 200. Number of Islands
    """DFS solution"""
    def numIslands(self, grid: List[List[str]]) -> int:
        # create a DS to store all answers
        count = 0
        
        # initialize DFS
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == "1":
                    count += self.dfs200(grid, r, c)
        
        # return 
        return count
    
    def dfs200(self, grid: List[List[str]], r: int, c: int) -> int:
        r_grid = len(grid)
        c_grid = len(grid[0])
        
        # base cases
        if r < 0 or c < 0 or r >= r_grid or c >= c_grid or grid[r][c] == "0":
            return 
        
        # process cell
        grid[r][c] = "0"
        
        # call DFS first
        self.dfs200(grid, r-1, c)
        self.dfs200(grid, r+1, c)
        self.dfs200(grid, r, c-1)
        self.dfs200(grid, r, c+1)
        
        # increament 
        return 1


    """ BFS solution - recommended for interview, showcasing your knowledge about memory usage difference between DFS and BFS """
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()     # contains (r,c)
        dq = deque([])
        count = 0
        
        # -------------------------------------
        def bfs():
            while dq: 
                r, c = dq.popleft()
                    
                # Loop through all neighbors
                directions = [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]
                for direction in directions:
                    nr, nc = direction
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        dq.append((nr, nc))
        # -------------------------------------
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Only start BFS on an unvisited land cell
                if grid[r][c] == "1" and (r, c) not in visited:
                    dq.append((r,c))
                    visited.add((r,c))
                    bfs()
                    count += 1
        
        return count 


    """ Iterative DFS solution """
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()     # contains (r,c)
        stack = []
        count = 0
        
        # -------------------------------------
        def iterativeDfs():
            while stack: 
                r, c = stack.pop()
                    
                # Loop through all neighbors
                directions = [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]
                for direction in directions:
                    nr, nc = direction
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        stack.append((nr, nc))
        # -------------------------------------
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Only start DFS on an unvisited land cell
                if grid[r][c] == "1" and (r, c) not in visited:
                    stack.append((r,c))
                    visited.add((r,c))
                    iterativeDfs()
                    count += 1
        
        return count 
    

    # --------------------------------------------------------------------------------------
    # Leetcode 1254. Number of Closed Islands
    def closedIsland(self, grid: List[List[int]]) -> int:
        # find all islands that touch boundary (they are not closed islands)
        for r in range (len(grid)): 
            if grid[r][0] == 0:
                self.dfs_closedIsland( [r, 0], grid ) # left
            if grid[r][len(grid[0]) - 1] == 0:
                self.dfs_closedIsland( [r, len(grid[0])-1], grid ) # right

        for c in range (len(grid[0])):
            if grid[0][c] == 0:
                self.dfs_closedIsland( [0, c], grid ) # top
            if grid[len(grid)-1][c] == 0:
                self.dfs_closedIsland( [len(grid)-1, c], grid ) # bottom

        # now all islands left are closed islands
        num_closed = 0
        for r in range (1, len(grid)-1):
            for c in range (1, len(grid[0])-1):
                if grid[r][c] == 0:
                    num_closed += 1
                    self.dfs_closedIsland( [r, c], grid ) 

        return num_closed
        """
        Time Complexity: O(row * col)
        Extra Space Complexity: O(1)
        """

    def dfs_closedIsland(self, coordinate: List[int], grid: List[List[int]]):
        r, c = coordinate
        # Base cases
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 
        if grid[r][c] == 1:
            return 

        # TO DO
        grid[r][c] = 1

        # Call DFS where needed
        self.dfs_closedIsland( [r-1, c], grid ) # top
        self.dfs_closedIsland( [r+1, c], grid ) # down
        self.dfs_closedIsland( [r, c-1], grid ) # left
        self.dfs_closedIsland( [r, c+1], grid ) # right
    

    # --------------------------------------------------------------------------------------
    # Leetcode 695. Max Area of Island
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        area = 0

        # call DFS on each grid cell
        for r in range ( len(grid) ):
            for c in range ( len(grid[0]) ):
                if grid[r][c] == 1:
                    area =  max(area, self.dfs_maxArea( [r,c], grid ) )

        return area
        """
        Time Complexity: O(row * cow)
        Extra Space Complexity: O(1)
        """

    # Initialize DFS
    def dfs_maxArea(self, coordinate: List[int], grid: List[List[int]]) -> int:
        r, c = coordinate
        # base cases
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 0
        if grid[r][c] == 0:
            return 0
        
        # TO DO
        grid[r][c] = 0
        count = 1
    
        # call DFS where needed
        count += self.dfs_maxArea( [r-1,c], grid ) # top
        count += self.dfs_maxArea( [r+1,c], grid ) # down
        count += self.dfs_maxArea( [r,c-1], grid ) # left
        count += self.dfs_maxArea( [r,c+1], grid ) # right

        return count
        

    # --------------------------------------------------------------------------------------------
    # Leetcode 827. Making A Large Island
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # Ex: 2 (island code) --> 5 (area of island 2)
        islandCodeToAreaMap = defaultdict(int)
        islandCode = 2
        area = 0
        # call DFS on each grid cell to compute the area of each island and override the value for that island
        for r in range ( len(grid) ):
            for c in range ( len(grid[0]) ):
                if grid[r][c] == 1:
                    area =  self.dfs_computeArea( [r,c], grid, islandCode)
                    # self.printMatrix(grid)
                    islandCodeToAreaMap[islandCode] = area
                    islandCode += 1

        # self.printMatrix(grid)
        print(islandCodeToAreaMap)

        # attemp to bridge each 0 cell to find the max area
        largestArea = area
        for r in range ( len(grid) ):
            for c in range ( len(grid[0]) ):
                if grid[r][c] == 0:
                    largestArea = max(largestArea, self.bridging([r,c], grid, islandCodeToAreaMap))
        
        return largestArea
        """
        Time Complexity: O(N^2) 
        """

    # DFS to compute the area of an island
    def dfs_computeArea(self, coordinate: List[int], grid: List[List[int]], islandCode: int) -> int:
        r, c = coordinate
        # base cases
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 0
        if grid[r][c] != 1:
            return 0
        
        # TO DO: mark cell as islandCode
        grid[r][c] = islandCode
        count = 1

        # call DFS on 4 directions to continue computing the area and marking cell as islandCode
        count += self.dfs_computeArea( [r-1,c], grid, islandCode ) # top
        count += self.dfs_computeArea( [r+1,c], grid, islandCode ) # down
        count += self.dfs_computeArea( [r,c-1], grid, islandCode ) # left
        count += self.dfs_computeArea( [r,c+1], grid, islandCode ) # right

        return count

    def bridging(self, coordinate: List[int], grid: List[List[int]], islandCodeToAreaMap: defaultdict(int)):
        r, c = coordinate
        largestArea = 1                 # [r,c] is a 0 cell, that means def have at least area of 1
        visitedIslands = set()

        # top
        if r-1 >= 0: 
            islandCode = grid[r-1][c]
            visitedIslands.add(islandCode)
            largestArea += islandCodeToAreaMap[islandCode]
        # down
        if r+1 <= (len(grid)-1):
            islandCode = grid[r+1][c]
            if islandCode not in visitedIslands:
                visitedIslands.add(islandCode)
                largestArea += islandCodeToAreaMap[islandCode]
        # left
        if c-1 >= 0:
            islandCode = grid[r][c-1]
            if islandCode not in visitedIslands:
                visitedIslands.add(islandCode)
                largestArea += islandCodeToAreaMap[islandCode]
        # right
        if c+1 <= (len(grid[0]) - 1):
            islandCode = grid[r][c+1]
            if islandCode not in visitedIslands:
                visitedIslands.add(islandCode)
                largestArea += islandCodeToAreaMap[islandCode]

        return largestArea

    # --------------------------------------------------------------------------------------
    # Leetcode 130. Surrounded Regions
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 

        m = len(board)
        n = len(board[0])

        # find all the 'O' on boundary and switch them into 'T' (Temporary)
        for r in range (m): 
            if board[r][0] == 'O':
                self.dfs_solve( [r, 0], board ) # left
            if board[r][n - 1] == 'O':
                self.dfs_solve( [r, n-1], board ) # right

        for c in range (n):
            if board[0][c] == 'O':
                self.dfs_solve( [0, c], board ) # top
            if board[m - 1][c] == 'O':
                self.dfs_solve( [m-1, c], board ) # bottom

        # switch all 'O' that don't touch boudary into 'X'
        for r in range (m):
            for c in range (n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
        """
        Time Complexity: O(row * col)
        Extra Space Complexity: O(1)
        """
                    
    def dfs_solve(self, coordinate: List[int], board: List[List[str]]):
        r, c = coordinate
        # Base cases
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return 
        if board[r][c] == 'X' or board[r][c] == 'T':
            return 

        # TO DO
        board[r][c] = 'T'

        # Call DFS where needed
        self.dfs_solve( [r-1, c], board ) # top
        self.dfs_solve( [r+1, c], board ) # down
        self.dfs_solve( [r, c-1], board ) # left
        self.dfs_solve( [r, c+1], board ) # right


    # --------------------------------------------------------------------------------------
    # Leetcode 417. Pacific Atlantic Water Flow
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        DFS for this problem takes: matrix, coordinate, previous value, ocean grid
        We don't have to send ans = [] along to record changes. All changes will be recorded in ocean parameter
        """

        # matrix is empty
        if not matrix: return []
        
        m = len(matrix)
        n = len(matrix[0])
        # create 2 Boolean matrixs for Pacific and Atlantic
        pacific = [[False for _ in range (n)] for _ in range (m)]
        atlantic = [[False for _ in range (n)] for _ in range (m)]

        # create a data structure to store answers
        # doesn't have to for this problem

        # Top-Pacific and Bottom-Atlantic
        for i in range(n):
            self.dfs_pacificAtlantic(matrix, [0, i], float('-inf'), pacific)
            self.dfs_pacificAtlantic(matrix, [m-1, i], float('-inf'), atlantic)
            
        # Left-Pacific and Right-Atlantic
        for i in range(m):
            self.dfs_pacificAtlantic(matrix, [i, 0], float('-inf'), pacific)
            self.dfs_pacificAtlantic(matrix, [i, n-1], float('-inf'), atlantic)

        # count satisfied coordinates
        ans = []
        for r in range (m):
            for c in range (n):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])
        
        return ans


    def dfs_pacificAtlantic(self, matrix: List[List[int]], coordinate: List[List[int]], prev: float, ocean: List[List[bool]]):
        r, c = coordinate
        m = len(matrix)
        n = len(matrix[0])
        # 3 base cases
        if r < 0 or c < 0 or r >= m or c >= n:
            return 
        if prev > matrix[r][c]:
            return  
        if ocean[r][c]: 
            return

        # TO DO
        ocean[r][c] = True

        # Call BFS as needed    
        top = [r-1, c]
        down = [r+1, c]
        left = [r, c-1]
        right = [r, c+1]

        self.dfs_pacificAtlantic(matrix, top, matrix[r][c], ocean)
        self.dfs_pacificAtlantic(matrix, down, matrix[r][c], ocean)
        self.dfs_pacificAtlantic(matrix, left, matrix[r][c], ocean)
        self.dfs_pacificAtlantic(matrix, right, matrix[r][c], ocean)


    # --------------------------------------------------------------------------------------
    # Leetcode 1020. Number of Enclaves
    def numEnclaves(self, A: List[List[int]]) -> int:
        count = 0

        # initialize DFS
        # first, initialize DFS for all boundary grids
        for m in range (len(A)): 
            if A[m][0] == 1: # left
                self.dfs_numEnclaves(A, m, 0)
            if A[m][len(A[0])-1] == 1: # right
                self.dfs_numEnclaves(A, m, len(A[0])-1)
        
        for n in range (len(A[0])):
            if A[0][n] == 1: # top
                self.dfs_numEnclaves(A, 0, n)
            if A[len(A)-1][n] == 1: # bottom
                self.dfs_numEnclaves(A, len(A)-1, n)

        # now, run dfs on all grids that do not touch boundary
        for r in range (1, len(A)-1):
            for c in range (1, len(A[0])-1):
                if A[r][c] == 1:
                    count += 1

        return count

    def dfs_numEnclaves(self, A: List[List[int]], r: int, c: int):
        # base cases
        if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]):
            return 
        if A[r][c] == 0:
            return 

        # TO DO
        A[r][c] = 0

        # call DFS where needed
        self.dfs_numEnclaves(A, r-1, c) # top
        self.dfs_numEnclaves(A, r+1, c) # down
        self.dfs_numEnclaves(A, r, c-1) # left
        self.dfs_numEnclaves(A, r, c+1) # right
        
    # Time: O(m*n)?
    # Space: O(1)

    # --------------------------------------------------------------------------------------
    # Leetcode 529. Minesweeper
    def adjacentMines(self, board: List[List[str]], click: List[int]) -> int:
        i, j = click
        
        num_mines = 0
        for r in range (i-1, i+2):
            for c in range (j-1, j+2):
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                    if board[r][c] == "M":
                        num_mines += 1

        return num_mines
                    

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        If click on "M" 
            -> game over
        else if click on "E"
            if no adjacent mines
                reveal it as "B"
            else
                digit 1->8
        
        """
        i, j = click
        
        # 1. If a mine ('M') is revealed, then the game is over - change it to 'X'
        if board[i][j] == 'M': 
            board[i][j] = 'X'
        # 2. If an empty square ('E') is revealed
        else: 
            # compute number of adjacent mines
            num_mines = self.adjacentMines(board, click)
            if num_mines: 
                board[i][j] = str(num_mines)
            else: 
                board[i][j] = "B"
                for r in range (i-1, i+2):
                    for c in range (j-1, j+2):
                        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] != "B":
                            self.updateBoard(board, [r, c])
                
        return board

    # --------------------------------------------------------------------------------------
    # Leetcode 1219. Path with Maximum Gold
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range (col)] for _ in range (row)]
        currentSum = 0
        maxGold = 0

        # -----------------------------------------------------------------------------------
        def dfs(coordinates: Tuple[int]) -> bool:
            nonlocal currentSum, visited, maxGold
            r,c = coordinates

            # Base cases: oob, no gold cell, or visited
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c: 
                return False
            if grid[r][c] == 0 or visited[r][c] == True: 
                return False

            # Todo
            visited[r][c] = True
            currentSum += grid[r][c]

            # DFS
            directions = [(r-1,c), (r,c+1), (r+1,c), (r,c-1)]   # up, right, down, left
            dirCount = 0
            for nr, nc in directions:
                coordinate = (nr, nc)
                if dfs(coordinate):
                    dirCount += 1

            # We will stop when we cannot collect any more gold 
            if dirCount == 0: 
                maxGold = max(maxGold, currentSum)

            # Backtrack
            visited[r][c] = False
            currentSum -= grid[r][c]

            return True
        # -----------------------------------------------------------------------------------

        for r in range (len(grid)):
            for c in range (len(grid[0])):
                # Attempt to start from any cell with gold
                if grid[r][c] != 0:
                    coordinate = (r,c)
                    dfs(coordinate)

        return maxGold

    # --------------------------------------------------------------------------------------
    # Leetcode 2664. The Knight’s Tour
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        visitedCells = 0                                # number of visited cells, act as counter too
        returnBoard = [[-1] * n for _ in range(m)]      # act as 'visited'
        
        # --------------------------------------
        def tryCell(row: int, col: int) -> bool:
            nonlocal visitedCells
            
            # Base cases:
            if visitedCells == m * n:
                return True
            if row < 0 or m <= row or col < 0 or n <= col:  # oob
                return False
            if returnBoard[row][col] != -1:                 # cell is already visited
                return False
            
            # Action
            returnBoard[row][col] = visitedCells
            visitedCells += 1        

            # Recursion
            directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for diffR, diffC in directions:
                nr = row + diffR
                nc = col + diffC
                if tryCell(nr, nc):
                    return True
                
            # Backtracking: whatever steps you do in Action, here you do them in reverse order
            visitedCells -= 1
            returnBoard[row][col] = -1
            
            # After failing to attempt all 8 directions
            return False
        # --------------------------------------
        tryCell(r,c)
        
        return returnBoard


    # --------------------------------------------------------------------------------------
    # Leetcode 36. Valid Sudoku
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set() for _ in range (9)]
        subBoxSets = [[set() for _ in range (3)] for _ in range (3)]

        for row in range (9):
            rowSet = set()
            for col in range (9):
                cell = ""
                if board[row][col] != ".":
                    cell = board[row][col]
                else:
                    continue

                # Case 1: Check each row
                if cell in rowSet:
                    return False
                else:
                    rowSet.add(cell)

                # Case 2: Check each column
                colSet = colSets[col]
                if cell in colSet:
                    return False
                else:
                    colSet.add(cell)

                # Case 3: Check each subbox
                subBoxRow = (row // 3)
                subBoxCol = (col // 3)
                subBoxSet = subBoxSets[subBoxRow][subBoxCol]
                if cell in subBoxSet:
                    return False
                else:
                    subBoxSet.add(cell)

        return True

    # --------------------------------------------------------------------------------------
    # Leetcode 37. Sudoku Solver
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Step 1: Fill all the sets
        fullSet = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        rowSets = [set() for _ in range (9)]
        colSets = [set() for _ in range (9)]
        subBoxSets = [[set() for _ in range (3)] for _ in range (3)]
        # visited = set()     # Contain all visited filled cell
        # emptyCell = 0

        for row in range (9):
            rowSet = rowSets[row]
            for col in range (9):
                cell = ""
                if board[row][col] != ".":
                    cell = board[row][col]
                else:
                    # emptyCell += 1
                    continue

                # Since the input is guaranteed to be solvable, we don't need to do any validation
                rowSet.add(cell)

                colSet = colSets[col]
                colSet.add(cell)

                subBoxRow = (row // 3)
                subBoxCol = (col // 3)
                subBoxSet = subBoxSets[subBoxRow][subBoxCol]
                subBoxSet.add(cell)

        # -------------------------------------------------------
        def placeCell(r: int, c: int) -> bool:
            # Base cases: Last column
            if c == 9:
                return placeCell(r+1, 0)
            # Base cases: Last row
            if r == 9:
                return True
            # Base cases: Filled cell
            if board[r][c] != ".":
                return placeCell(r,c+1)

            # Action
            rowSet = rowSets[r]
            potentialValuesRow = fullSet.difference(rowSet)
            colSet = colSets[c]
            potentialValuesCol = fullSet.difference(colSet)
            subBoxSet = subBoxSets[r//3][c//3]
            potentialValuesSubBox = fullSet.difference(subBoxSet)

            potentialValues = potentialValuesRow.intersection(potentialValuesCol).intersection(potentialValuesSubBox)
            print("For row {} and col {}, the potentialValues are {}".format(r, c, potentialValues))

            # Try each potential value
            for value in potentialValues:
                board[r][c] = value
                rowSets[r].add(value)
                colSets[c].add(value)
                subBoxSets[r//3][c//3].add(value)

                # DFS the next cell
                if placeCell(r,c+1):
                    return True
                
                # Backtracking
                board[r][c] = "."
                rowSets[r].remove(value)
                colSets[c].remove(value)
                subBoxSets[r//3][c//3].remove(value)
                
            # After attempting all values from 0->9, it means this Sudoku cannot be solved
            return False
        # -------------------------------------------------------

        # Step 2: Recursion and Backtracking
        placeCell(0,0)
        self.print_sudoku(board)

    def print_sudoku(self, board: List[List[int]]) -> None:
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Horizontal separator

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")  # Vertical separator

                val = board[i][j]
                print(val if val != 0 else ".", end=" ")

            print()  # Newline after each row


    # --------------------------------------------------------------------------------------------
    # Leetcode 79. Word Search
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False

        # Optimization: if the last char frequency is less than first char frequency, reverse word so less path to explore
        wordCounter = Counter(word)
        if wordCounter[word[-1]] < wordCounter[word[0]]:
            word = word[::-1]

        # Create an expanded board to hold a bool for each cell, which represents if the cell is visited or not
        expandedBoarded = [ [[] for _ in range (len(board[0]))] for _ in range (len(board)) ]
        # print(expandedBoarded)
        for r in range (len(board)):
            for c in range (len(board[0])):
                expandedBoarded[r][c] = [board[r][c], False]

        result = False

        # Initialize DFS
        for r in range (len(expandedBoarded)):
            for c in range (len(expandedBoarded[0])):
                if expandedBoarded[r][c][0] == word[0]:
                    result = result or self.dfs([r,c], expandedBoarded, word, 0)
                    # Optimization: exit early if needed
                    if result: 
                        return True

        return result

    def dfs (self, coordinate: List[int], board: List[List[str]], word: str, idx: int) -> bool:
        r,c = coordinate

        # Base case 1: This base case has to be put first in checking order
        if idx == len(word):
            return True
        # Base case 2:
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]): 
            return False
        # Base case 3:
        if board[r][c][0] != word[idx] or board[r][c][1]:
            return False

        # mark the cell as visited
        board[r][c][1] = True
        # dfs
        left = self.dfs([r,c-1], board, word, idx+1)
        up = self.dfs([r-1,c], board, word, idx+1)
        right = self.dfs([r,c+1], board, word, idx+1)
        down = self.dfs([r+1,c], board, word, idx+1)
        # backtracking
        board[r][c][1] = False

        return (left or up or right or down)


    # --------------------------------------------------------------------------------------------
    # Leetcode 212. Word Search II
    # Trie + DFS
    def addWord(self, word: str, root: TrieNode):
        current = root
        # loop through each char
        for c in word:
            if c not in current.children:
                # create new node
                current.children[c] = TrieNode()
            current = current.children[c]
        
        # mark the last node as end of the word
        current.isEnd = True

    def dfs (self, coordinate: List[int], board: List[List[str]], node: TrieNode, visited: set(), result: set(), potential: str):
        r,c = coordinate

        # Base case 1: out of bounce
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]): 
            return
        # Base case 2: char is not a start of any word or cell is already visited
        if board[r][c] not in node.children or (r,c) in visited:
            return

        node = node.children[board[r][c]]       # update node
        visited.add((r,c))                      # mark the cell as visited
        potential += board[r][c]                # add one more char to the potential
        if node.isEnd:  
            result.add(potential)
            # return  <-- cannot return here
       
        # dfs
        self.dfs([r,c-1], board, node, visited, result, potential)      # left
        self.dfs([r-1,c], board, node, visited, result, potential)      # up
        self.dfs([r,c+1], board, node, visited, result, potential)      # right
        self.dfs([r+1,c], board, node, visited, result, potential)      # down
        # backtracking
        visited.remove((r,c))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # corner cases
        if not board or not words: return []

        # create DS to store the result: root TrieNodes + sets
        root = TrieNode()
        for word in words:
            self.addWord(word,root)
        result = set()
        visited = set()

        # call DFS on each cell
        for r in range (len(board)):
            for c in range (len(board[0])):
                # if char in board[r,c] isnt't a start of any word, this dfs call will simply return right away at base case #2
                self.dfs([r,c], board, root, visited, result, "")

        return list(result)


    # --------------------------------------------------------------------------------------------
    # Leetcode 51. N-Queens
    # Idea: On each row, attempt to place one Queen in a column, and keep going down row by row until cannot place another Queen.
    # Then backtrack and attempt to place one Queen in the next column.
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [[0 for _ in range (n)] for _ in range (n)]
        solutions = []

        # Attempt to place a Queen on 0-th row
        self.placeQueen(matrix, 0, solutions)
        
        # If not successful, this means this matrix n x n cannot be solved for N-Queens problem
        print("There are {} solutions.".format(len(solutions)))
        return solutions
    
    # Helper fn to attemtp to place a Queen on a specific row
    def placeQueen(self, matrix: List[List[int]], row: int, solutions: List[int]):
        n = len(matrix)      # n is num of rows/cols

        # Base case: Everytime we hit this base case, it means we found a solution
        if row == n:
            board = []
            for r in matrix:
                row_str = ''.join('Q' if cell == 1 else '.' for cell in r)
                board.append(row_str)
            solutions.append(board)
            # Here if you retrun True, the call stack will bubble up to the root and return after exploring only the first branch of the tree
            return      

        for col in range (n):
            if self.isSafe(matrix, row, col):
                matrix[row][col] = 1

                # After being able to place a Queen on matrix[row][col], attempt to
                # place the next Queen on row+1
                if self.placeQueen(matrix, row+1, solutions):
                    return True
                
                # Backtracking part
                matrix[row][col] = 0

        return False

    # Helper fn to attemtp to place a Queen on a specific cell
    # We can definitely optimize on isSafe() helper fn
    def isSafe(self, matrix: List[List[int]], row: int, col: int):
        n = len(matrix)      # n is num of rows/cols

        # Case 1: Check above vertical line
        for r in range (row-1, -1, -1):
            if matrix[r][col] == 1:
                return False
            
        # Case 2: Check above left diagonal line
        for r,c in zip( range(row-1, -1, -1), range(col-1, -1, -1) ):
            if 0 <= r < n and 0 <= c < n and matrix[r][c] == 1:
                return False

        # Case 3: Check above right diagonal line
        for r,c in zip( range(row-1, -1, -1), range(col+1, n) ):
            if 0 <= r < n and 0 <= c < n and matrix[r][c] == 1:
                return False

        return True


    # --------------------------------------------------------------------------------------------
    # Leetcode 52. N-Queens II
    def totalNQueens(self, n: int) -> int:
        return len(self.solveNQueens(n))


if __name__ == "__main__":
    leetcode = Solution()

    # ------------------------------------------
    # n = 3
    # expected = ["((()))","(()())","(())()","()(())","()()()"]
    # combinations = leetcode.generateParenthesis(3)
    # print(combinations)
    # assert combinations == expected

    # ------------------------------------------
    # matrix = [[1,2,2,3,5], 
    #           [3,2,3,4,4], 
    #           [2,4,5,3,1], 
    #           [6,7,1,4,5],
    #           [5,1,1,2,4] ]
    # coordinates = leetcode.pacificAtlantic(matrix)

    # print(coordinates)

    # -------------------------------------------
    # A = [ [0,0,0,0],
    #       [1,0,1,0],
    #       [0,1,1,0],
    #       [0,0,0,0] ]
    # ans = leetcode.numEnclaves(A)
    # print(ans)


    # -------------------------------------------
    # deadends = ["0201","0101","0102","1212","2002"] 
    # target = "0202"

    # min_turns = leetcode.openLock_2025(deadends, target)
    # print(min_turns)


    # ------------------------ 695: Max Area of Island -------------------------
    # grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    #         [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #         [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #         [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #         [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #         [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #         [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #         [0,0,0,0,0,0,0,1,1,0,0,0,0] ]

    # max_area = leetcode.maxAreaOfIsland(grid)
    # print(max_area)


    # ------------------------- 1254: Number of Closed Islands -------------------------
    # grid = [[1,1,1,1,1,1,1,0],
    #         [1,0,0,0,0,1,1,0],
    #         [1,0,1,0,1,1,1,0],
    #         [1,0,0,0,0,1,0,1],
    #         [1,1,1,1,1,1,1,0] ]
    # num_closed_island = leetcode.closedIsland(grid)
    # print(num_closed_island)

    # ------------------------- 93. Restore IP Addresses -------------------------
    s = "25525511135"
    leetcode.restoreIpAddresses(s)

    # ------------------------- 39. Combination Sum -------------------------
    # candidates = [2,3,6,7]
    # ans = leetcode.combinationSum_backtrack(candidates)
    # print(ans)

    # candidates = [10,1,2,7,6,1,5]
    # print( leetcode.combinationSum2(candidates, 8) )


    # ------------------------- Permutation -------------------------
    # nums = [1,2,3]
    # ans = leetcode.permute(nums)
    # print(ans)

    # ------------------------ 827. Making A Large Island -------------------------
    # grid = [[0,0,1,1],
    #         [0,0,0,1],
    #         [1,0,0,0],
    #         [1,1,0,0]]
    
    # grid = [[1,1],[1,1]]

    # largeIsland = leetcode.largestIsland(grid)
    # print(largeIsland)

    # ------------------------ 827. Making A Large Island -------------------------
    # grid = [[0,6,0],[5,8,7],[0,9,0]]
    # print(leetcode.getMaximumGold(grid))

    # ------------------------ 36. Valid Sudoku ------------------------
    # board = [["8","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]
    # print(leetcode.isValidSudoku(board))

    # ------------------------ 37. Sudoku Solver ------------------------
    # placeCell(0,0)
    # board = [["5","3",".",".","7",".",".",".","."],
    #          ["6",".",".","1","9","5",".",".","."],
    #          [".","9","8",".",".",".",".","6","."],
    #          ["8",".",".",".","6",".",".",".","3"],
    #          ["4",".",".","8",".","3",".",".","1"],
    #          ["7",".",".",".","2",".",".",".","6"],
    #          [".","6",".",".",".",".","2","8","."],
    #          [".",".",".","4","1","9",".",".","5"],
    #          [".",".",".",".","8",".",".","7","9"]]
    # leetcode.solveSudoku(board)

    # ------------------------ 79. Word Search -------------------------
    # grid = [["A","B","C","E"],
    #         ["S","F","C","S"],
    #         ["A","D","E","E"]]
    # word = "ABCCED"

    # print(leetcode.exist(grid, word))


    # ------------------------ 51. N-Queens -------------------------
    # ans51 = leetcode.solveNQueens(5)
    # for matrix in ans51:
    #     for row in matrix:
    #         print(row)
    #     print("-----")