"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================= Leetcode Exercises Sorting Algorithms =========================================
1. Leetcode 1329. Sort the Matrix Diagonally
2. Leetcode 1366. Rank Teams by Votes
3. Leetcode 853. Car Fleet
4. Leetcode 1451. Rearrange Words in a Sentence
5. Leetcode 56. Merge Intervals

"""

from typing import List

class Solution:
    # Leetcode 1329. Sort the Matrix Diagonally
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # deal with bottom left
        for k in range (m):
            diagonals = []
            # first, get that diagonal into a list
            i = k
            j = 0
            while i < m and j < n:
                diagonals.append(mat[i][j])
                i += 1
                j += 1

            print(diagonals)
            # sort that diagonal
            diagonals.sort()

            # then, put it back into mat
            i = k
            j = 0
            while i < m and j < n:
                mat[i][j] = diagonals[j]
                i += 1
                j += 1
        
        # deal with top right
        for k in reversed (range(m)):
            diagonals = []
            # first, get that diagonal into a list
            i = k
            j = n-1
            while i >= 0 and j >= 0:
                diagonals.append(mat[i][j])
                i -= 1
                j -= 1

            print(diagonals)
            # sort that diagonal
            diagonals.sort()

            # then, put it back into mat
            i = k
            j = n - 1
            while i >= 0 and j > i:
                mat[i][j] = diagonals.pop()
                i -= 1
                j -= 1

        return mat

    # Leetcode 1366. Rank Teams by Votes
    def rankTeams(self, votes: List[str]) -> str:
        number_of_teams = len(votes[0])
        
        # has a form of: { name of team 1: [votes], name team 2: [votes] }
        team_counter = {}
        
        # finish the format
        for i in range (number_of_teams):    
            team_counter[votes[0][i]] = [0] * number_of_teams
        
        # count votes
        for vote in votes:
            for i in range (len(vote)):
                team_counter[vote[i]][i] += 1

        # print(team_counter)

        # sort dict by values
        # first sort the IDs
        res = { team: votes for team, votes in sorted( team_counter.items(), key = lambda item: item[0] ) }
        # then sort the votes
        res = [ team for team, votes in sorted( res.items(), key = lambda item: item[1], reverse=True ) ]

        return "".join(res)
            
    # Leetcode 853. Car Fleet
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]

        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'

        return ans + len(times) # remaining car is fleet (if it exists)

    # Leetcode 1451. Rearrange Words in a Sentence
    def arrangeWords(self, text: str) -> str:
        # list of each word
        text_list = text.split()
        text_list[0] = text_list[0].lower()

        # now construct list of index and length of each word
        len_list = []
        index_list = []
        for i in range (len(text_list)):
            len_list.append(len(text_list[i]))
            index_list.append(i)

        # zip
        words = list(zip(text_list, index_list, len_list))

        #print("Pre-sorted: ", words)

        # now sort
        words.sort( key=lambda x: [ x[2], x[1] ] )

        #print("After sorted: ", words)

        # extract text and capitalize the first word
        text_list = [ word for (word, _, _) in words ]
        text_list[0] = text_list[0].capitalize()

        return " ".join(text_list)

    # Leetcode 56. Merge Intervals
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # i = 1
    # result = [[1,6],[8,10],]
    # leftInterval = [1,3]
    # rightInterval = [2,6]
    # newInterval = [1,6]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda x: [x[0]])  # sort intervals by their start time
        print(intervals)
        result.append(intervals[0])

        for i in range(len(intervals)-1):
            # If the start time of the following interval is smaller or equal to the end time of current interval -> merge
            if intervals[i+1][0] <= result[-1][1]: 
                leftInterval = result.pop()
                rightInterval = intervals[i+1]
                newInterval = [leftInterval[0], max(leftInterval[1], rightInterval[1])]     # pay attention to the end time of the new interval
                result.append(newInterval)
            else:
                result.append(intervals[i+1])

        print("result56: ", result)
        return result


# ===================================================================================================================







if __name__ == "__main__":
    leetcode = Solution()

    # -------------------------------------------------------------------------------------------
    #lc1329 = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    # lc1329 = [[11,12,8,4],[10,1,2,3],[9,5,6,7]]
    #sort_diag = leetcode.diagonalSort(lc1329)
    #print(sort_diag)

    # -------------------------------------------------------------------------------------------
    # lc1366 = ["BCA","CAB","CBA","ABC","ACB","BAC"]
    # teams_1366 = leetcode.rankTeams(lc1366)
    # print(teams_1366)

    # -------------------------------------------------------------------------------------------
    # lc853_target = 12
    # lc853_p = [10,8,0,5,3]
    # lc853_speed = [2,4,1,1,3]

    # print(leetcode.carFleet(lc853_target, lc853_p, lc853_speed))

    # -------------------------------------------------------------------------------------------
    # text = "Keep calm and code on"
    # text = leetcode.arrangeWords(text)
    # print(text)

    # ------------------------------------ 56 ------------------------------------
    intervals = [[1,3],[2,6],[8,10],[15,18],[16,17]]
    leetcode.merge(intervals)


