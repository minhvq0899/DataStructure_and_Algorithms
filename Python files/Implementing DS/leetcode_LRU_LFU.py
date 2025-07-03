"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Implement LRU and LFU =========================================================

1. Leetcode 146: LRU Cache
    https://www.romaglushko.com/blog/design-lru-cache/
     
2. Leetcode 895. Maximum Frequency Stack (Hard)
3. Leetcode 460: LFU Cache (Hard)

"""

import collections
from typing import List

"""
Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
"""
# Leetcode 146. LRU Cache ------------------------------------------------------------------------------
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = collections.defaultdict(LinkedListNode)
        self.linkedlist = LinkedList()

    def printDS(self, action: str, key: int):
        print(action + str(key))

        # print map
        for k,v in self.map.items():
            print("Key:{} - Value:||{}||".format(k,v))
        
        # print linkedlist
        self.linkedlist.printList()
        print("head: ", self.linkedlist.head)
        print("tail: ", self.linkedlist.tail)
        print("----------------------------------------------------------------------")
        
    def get(self, key: int) -> int:
        self.printDS("get()", key)
        if key in self.map:
            node = self.map[key]
            self.linkedlist.moveToHead(node)
            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        self.printDS("put()", key)
    
        node = None
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.linkedlist.moveToHead(node)
            return
        else:
            node = LinkedListNode(key, value)

        # if we reach cap, evict the least recently used
        if len(self.map) == self.cap:
            # get the tail node
            tail = self.linkedlist.tail
            # delete the key in the map
            if tail: 
                del self.map[tail.key]
            # delete the tail node
            self.linkedlist.deleteTail()

        # eventually, insert the new key at head of the linkedlist
        self.linkedlist.insertHead(node)
        # insert new key in map
        self.map[key] = node

class LinkedListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return "Key:{} - Value:{}".format(self.key, self.value)

class LinkedList:
    # head will be the most recently used item
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self): 
        current = self.head 
        forward = ""
        while (current):
            s = str(current) + " ->" 
            forward += s
            current = current.next
        
        current = self.tail
        backward = ""
        while (current):
            s = str(current) + " ->" 
            backward += s
            current = current.prev

        print("forward: " + forward)
        print("backward: " + backward)
        
    
    # insert at the head O(1)
    def insertHead(self, node: LinkedListNode):
        # case 1: empty list
        if not self.head: 
            self.head = node
            self.tail = node
        # case 2: linkedlist has len >= 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # delete at the tail O(1)
    def deleteTail(self):
        # case 1: list empty
        if not self.tail: return 

        # case 2: list has len 1
        if self.head == self.tail:
            del self.tail
            self.head = None
            self.tail = None
            return

        # case 3: list has len >= 2
        temp = self.tail.prev
        del self.tail
        temp.next = None
        self.tail = temp

    # move a node to head O(1)
    def moveToHead(self, node: LinkedListNode):
        # case 1: node is already head
        if self.head == node:
            return

        # case 2: node is tail
        if self.tail == node:
            # prepare tail
            self.tail = node.prev
            self.tail.next = None
        # case 3: node is somewhere in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        # mutual for both step 2 + 3: prepare head
        node.next = self.head
        self.head.prev = node
        node.prev = None
        # assign
        self.head = node


# Leetcode 895. Maximum Frequency Stack (Hard) ------------------------------------------------------------------------------
class FreqStack:
    def __init__(self):
        self.countStackMap = collections.defaultdict(list)
        self.maxCount = 0
        self.valueCountMap = collections.defaultdict(int)

    def push(self, val: int) -> None:
        # In python defaultdict, if key val is not in the dict, the value will be 0 instead of access error
        currentCount = 1 + self.valueCountMap[val]
        self.valueCountMap[val] = currentCount

        # update global maxCount if needed
        if currentCount > self.maxCount:
            self.maxCount = currentCount

        # update the countStack mapping
        self.countStackMap[currentCount].append(val)

    def pop(self) -> int:
        # we want to pop a val with the max freq
        val = self.countStackMap[self.maxCount].pop()
        self.valueCountMap[val] -= 1

        # if we just pop the last element on the maxCount level, decrement maxCount
        if len(self.countStackMap[self.maxCount]) == 0:
            del self.countStackMap[self.maxCount]
            self.maxCount -= 1

        return val


# Leetcode 460: LFU cache (Hard) ------------------------------------------------------------------------------
class NodeLFU:
    def __init__(self, key: int, value: int, count=1):
        self.key = key
        self.value = value
        self.cnt = count
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return "Key:{},Value:{},Cnt:{}".format(self.key, self.value, self.cnt)

class LinkedListLFU:
    # head will be the most recently used item
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self): 
        current = self.head 
        forward = ""
        while (current):
            s = str(current) + " ->" 
            forward += s
            current = current.next
        
        current = self.tail
        backward = ""
        while (current):
            s = str(current) + " ->" 
            backward += s
            current = current.prev

        return "forward: " + forward + "\nbackward" + backward
        
    # insert at the head O(1)
    def insertHead(self, node: NodeLFU):
        # case 1: empty list
        if not self.head: 
            self.head = node
            self.tail = node
        # case 2: linkedlist has len >= 1
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

    # delete at the tail O(1) and return the key deleted
    def deleteTail(self) -> int:
        # case 1: list empty
        if not self.tail: return None

        returnKey = self.tail.key
        # case 2: list has len 1
        if self.head == self.tail:    
            del self.tail
            self.head = None
            self.tail = None
        # case 3: list has len >= 2
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        return returnKey
            

    # delete a node O(1)
    def delete(self, node: NodeLFU):
        # edge cases
        if not node or not self.head: return 

        # case 1: node is head
        if self.head == node:
            self.head = node.next
            # 1.1. list has len > 1
            if self.head:
                self.head.prev = None
            # 1.2. list has len 1 -> after deleting head, list becomes empty
            else:
                self.tail = None 
        # case 2: node is tail
        elif self.tail == node:
            self.deleteTail()
        # case 3: node is somewhere in the middle
        else:
            if node.prev: node.prev.next = node.next
            if node.next: node.next.prev = node.prev
            del node

    # return True if the LL is empty
    def isEmpty(self) -> bool:
        return (self.head == None) and (self.tail == None)

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 1
        self.keyNodeMap = collections.defaultdict(NodeLFU)
        self.freqLLMap = collections.defaultdict(LinkedListLFU)

    def printDS(self, action: str, key: int):
        print(action + str(key))
        print("Size: " + str(self.size) + "; minFreq: " + str(self.minFreq))

        # print map
        print("self.keyNodeMap")
        for k,v in self.keyNodeMap.items():
            print("\tKey:{} - Value:||{}||".format(k,v))

        print("self.freqLLMap")
        for k,v in self.freqLLMap.items():
            print("\tFreq:{} - LinkedList:||{}||".format(k,v))
            print("\thead: ", v.head)
            print("\ttail: ", v.tail)

        print("----------------------------------------------------------------------")

    # Note: we will delete the old node, and create a new node before setting it's next and prev property to avoid stale ref
    def updateCntAndUpdateFreqMap(self, node: NodeLFU, newValue = None):
        ogCnt = node.cnt
        newNode = None
        # when we create a new node for get()
        if not newValue:
            newNode = NodeLFU(node.key, node.value, ogCnt+1)
        # when we create a new node for put()
        else:
            newNode = NodeLFU(node.key, newValue, ogCnt+1)

        # delete node from the og LL
        ogLinkedList = self.freqLLMap[ogCnt]
        ogLinkedList.delete(node)

        # Update self.minFreq if needed
        if ogCnt == self.minFreq and ogLinkedList.isEmpty():
            self.minFreq += 1

        # insert node to head of the new LL
        newLinkedList = self.freqLLMap[ogCnt+1]
        newLinkedList.insertHead(newNode)

        # update self.keyNodeMap
        self.keyNodeMap[newNode.key] = newNode
        

    def get(self, key: int) -> int:
        self.printDS("get() - ", key)

        if key in self.keyNodeMap:
            # retrieve the node and update info
            node = self.keyNodeMap[key]
            self.updateCntAndUpdateFreqMap(node)
            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        self.printDS("put() - ", key)

        # case 1: when key exists in the mapping
        if key in self.keyNodeMap: 
            # retrive node
            node = self.keyNodeMap[key]
            self.updateCntAndUpdateFreqMap(node, value)
            return 
        
        # case 2: when key doesn't exist in the mapping yet
        # ---- special case: when the cache reach its limit ----
        if self.size == self.cap:
            # find the LRU key among the LFU key
            minFreqLinkedList = self.freqLLMap[self.minFreq]
            popKey = minFreqLinkedList.deleteTail()
            del self.keyNodeMap[popKey]
            # update LFU's size
            self.size -= 1
            # no need to update self.minFreq here, as we will reset it aftet adding the new node below
            
        # ---- now we are ready to add ----
        node = NodeLFU(key,value)
        self.keyNodeMap[key] = node # add to keyNodeMap
        linkedList = self.freqLLMap[1]
        linkedList.insertHead(node) # add to freqLLMap
        self.size += 1 # update LFU's size
        self.minFreq = 1 # update self.minFreq

















if __name__ == "__main__":
    # Leetcode 146: LRU
    """
    lruCache = LRUCache(3)
    lruCache.put(1,1)
    lruCache.put(2,2)
    lruCache.put(3,3)
    lruCache.put(4,4)
    print(lruCache.get(4))
    print(lruCache.get(3))
    print(lruCache.get(2))
    print(lruCache.get(1))
    lruCache.put(5,5)
    print(lruCache.get(1))
    print(lruCache.get(2))
    print(lruCache.get(3))
    print(lruCache.get(4))
    print(lruCache.get(5))
    """

    # ----------------------------------------------------------
    # Leetcode 895. Maximum Frequency Stack (Hard)
    """
    freqStack = FreqStack()
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)
    freqStack.pop()
    freqStack.pop()
    freqStack.pop()
    freqStack.pop()
    """

    # ----------------------------------------------------------
    # Leetcode 460: LFU
    lfu = LFUCache(3)
    lfu.put(2, 2)
    lfu.put(1, 1)
    lfu.get(2)
    lfu.get(1)
    lfu.get(2)
    lfu.put(3, 3)
    lfu.put(4, 4)
    lfu.get(3)
    lfu.get(2)
    lfu.get(1)
    lfu.get(4)













