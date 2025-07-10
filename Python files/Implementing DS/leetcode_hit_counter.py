"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= 362. Design Hit Counter =========================================================
"""

from collections import deque


# Leetcode 362. Design Hit Counter
class HitCounter:
    def __init__(self):
        # Queue to store (timestamp, count) pairs
        self.hits = deque()
        self.total = 0  # Total number of hits in the current 5-minute window

    def hit(self, timestamp: int) -> None:
        # If the last recorded timestamp is the same, increment its count
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            # Otherwise, append a new timestamp with count 1
            self.hits.append([timestamp, 1])
        self.total += 1  # Update total hits

    def getHits(self, timestamp: int) -> int:
        # Remove outdated hits (older than 300 seconds)
        while self.hits and timestamp - self.hits[0][0] >= 300:
            old_time, count = self.hits.popleft()
            self.total -= count  # Subtract outdated hits from total
        return self.total


if __name__ == "__main__":







