"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Implement Router and Magic Dictionary =========================================================

Leetcode 3508. Implement Router
Leetcode 676. Implement Magic Dictionary

"""

import collections
from typing import List
import queue
import bisect

# --------------------------------------------------------------------------------------------------------------------
# Leetcode 3508. Implement Router
class Packet:
    def __init__(self, source: int, destination: int, timestamp: int):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp

    def __str__(self):
        return ( "{}s{}d{}t".format(str(self.source), str(self.destination), str(self.timestamp)) )

class Router:
    def __init__(self, memoryLimit: int):
        self.cap = memoryLimit
        self.size = 0
        self.queue = queue.Queue()
        self.destTimestampsMap = collections.defaultdict(list)
        self.packetSet = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # create a packet
        packet = Packet(source, destination, timestamp)

        # check for dup
        packetStr = str(packet)
        if packetStr in self.packetSet:
            return False
        
        # check for limit exceed
        if self.size == self.cap:
            self.forwardPacket()
        
        # add the packet to queue, set, and our dicts
        self.queue.put(packet)
        self.packetSet.add(packetStr)
        self.destTimestampsMap[destination].append(timestamp)

        # increase size
        self.size += 1
        
        return True

    def forwardPacket(self) -> List[int]:
        if self.queue.empty():
            return []
        
        # get packet
        packet = self.queue.get()

        # remove the timestamp of the packet being removed
        self.destTimestampsMap[packet.destination].remove(packet.timestamp)
        self.packetSet.remove( str(packet) )
        self.size -= 1

        return [packet.source, packet.destination, packet.timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        increasingTimestamps = self.destTimestampsMap[destination]
        if not increasingTimestamps:
            return 0

        startIdx = bisect.bisect_left(increasingTimestamps, startTime)
        endIdx = bisect.bisect_right(increasingTimestamps, endTime)

        return len( increasingTimestamps[startIdx:endIdx] )
    


if __name__ == "__main__":
    # -----------------------------------------------------
    # Leetcode 3508. Implement Router
    router = Router(3)
    router.addPacket(1,4,90)
    router.addPacket(2,5,90)
    router.addPacket(1,4,90)
    router.addPacket(3,5,95)
    router.addPacket(4,5,105)
    router.forwardPacket()
    router.addPacket(5,2,110)
    router.getCount(5,100,110)














