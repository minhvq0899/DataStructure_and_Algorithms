# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from typing import List

# Minh Quang Vũ
# Vì em không biết có được dùng thư viện hoặc function có sẵn của python hay không
# nên em sẽ tránh không dùng
# Thay vào đó em sẽ dùng class Merge Sort em tự viết
# Chúng ta sẽ dùng Merge Sort ( O(nlogn) worst case )
class Merge:
    aux = []
    def merge(self, a: List[int], lo: int, mid: int, hi: int):
        self.aux = [None] * (hi - lo)
        i = lo
        j = mid
        N = hi
        for k in range (0, len(self.aux)):
            if i == mid: # run out of element in above halve
                self.aux[k] = a[j]
                j += 1
            elif j == hi: # run out of element in below halve
                self.aux[k] = a[i]
                i += 1
            elif a[i] <= a[j]: 
                self.aux[k] = a[i]
                i += 1
            else:
                self.aux[k] = a[j]
                j += 1
        
        # now just have to copy everything from aux into array a
        for k in range (0, len(self.aux)):
            a[lo + k] = self.aux[k]

    # helper function that does the whole thing
    def sort(self, a: List[int], lo: int, hi: int):
        N = hi - lo
        # base case
        if N <= 1: 
            return # this mean the array only has one or less number of element
        mid = lo + math.ceil(N/2)
        self.sort(a, lo, mid)
        self.sort(a, mid, hi)
        self.merge(a, lo, mid, hi)

    # actual call
    def merge_sort(self, a: List[int]):
        self.sort(a, 0, len(a))



class Solution:
    def marathon_runner_ranking(self, inputs: List[List[int]]) -> int:
        #print("OG input ", inputs)
        # inputs có dạng [ [finish, start], [], [], ... ]
        # inputs.sort( key = lambda x: x[0] )
        # sort để biết rank nếu tính theo luật cũ
        Merge().merge_sort(inputs) # O(nlogn) in worst case
        #print("After sort for old rank ", inputs)
        
        
        # giờ ta đánh rank cũ
        for i in range ( len(inputs) ): # O(n)
            inputs[i].append( i+1 )
            # tính thời gian chạy và lưu thời gian chạy vào phần tử đầu 
            # tiên để sau đó ta sort
            inputs[i][0] = inputs[i][0] - inputs[i][1] 
        #print("Add old rank and run time ", inputs)
            
        
        # inputs.sort( key=lambda x: x[0])
        # sort để biết rank mới nếu tính theo luật mới
        Merge().merge_sort(inputs) # O(nlogn) in worst case
        #print("After sort for new rank: ", inputs)
        
        
        # đánh rank mới rồi tính tổng thay đổi luôn
        change = 0
        for i in range ( len(inputs) ): # O(n)
            inputs[i].append( i+1 )
            change += abs( inputs[i][3] - inputs[i][2] )
        #print(inputs)
            
        return change
    

        
if __name__ == "__main__":
    inputs = []
    
    while True:
        try:
            a, b = input().strip().split(' ')
            # ta để finish time lên đầu để tẹo nữa sort (vì function sort ta viết
            # sort bằng phần tử đầu tiên)
            inputs.append( [int(b), int(a)] )
        except (EOFError):
            break        
    
    # ------------------------------------
    
    solution = Solution()
    print( solution.marathon_runner_ranking(inputs) )
    