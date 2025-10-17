"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= 901. Online Stock Span =========================================================
Monotonic stack
Difference from other Monotonic problems: the input for this problem is a data stream

Idea
Example: 
prices = [100, 80, 60, 70, 60, 75, 85]
spans = [1, 1, 1, 2, 1, 4, 6]
On 7th day (index 6), with price 85, there can be two cases:

1. prices[i] (85) >= prices[i-1] (in this case it's 75)
--> We can reuse the 'span' info from the previous day, which is stored like this (price, span)
In this case, 'span' here holds info as number of consecutive days prior to day (i-1)th that price is <= 'price'
And since 'price' <= price[i], we know that price[i] >= all the prices 'span' number of days prior to (i-1)th day
--> We can discard (pop) this info from our stack, because we are about to append into our stack this new info (price[i], 1+'span'+X),
where X is the number of days prior to (i-1)th day with price > 'price' but < 'price[i] (85)

2. prices[i] (85) < prices[i-1]
--> new start, appending (price, 1) to stack

Watch this youtube vid for better explaination
https://www.youtube.com/watch?v=slYh0ZNEqSw

"""

from typing import List
from collections import defaultdict


class StockSpanner:
    def __init__(self):
        self.stack = []             # (price, # of span day)
        
    def next(self, price: int) -> int:
        print(self.stack)

        # Scenario 2 as described above
        # For optimization, this if block can be omitted. But I still include here so we better understand the logic
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, 1))
            return 1

        # Scenario 1
        # Step 1: Keep the stack order as decreasing
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, poppedSpan = self.stack.pop()
            span += poppedSpan

        # Step 2: Update stack
        self.stack.append((price, span))

        # Step 3: return
        return span
    











        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

