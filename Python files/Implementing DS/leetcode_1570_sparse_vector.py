"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= 1570. Dot Product of Two Sparse Vectors =========================================================
This question is often asked during Meta interviews. 

Solution 1 - O(N)
    - Store our vector 'nums' as a HashMap. Key is index of non-zero element, Value is the element
    - However, Meta might not prefer HashMap because of a few reasons:
        + HashMap can be slow due to collision (few ways to handle collision are 1.Separate chaining 2.Open addressing 3.Cuckoo hashing)
        + We need to care about bunch of variables: bucket size (wrong bucket size can lead to either slow look-up or memory overhead), load factor, etc
        + We need to care about memory management. A few foundational memory management concepts in operating systems, allocators, and high-performance caches are:
            * Slab allocator & Slab class sizes
            * Buddy allocator
        + We need to care about concurrency - Spin lock vs Mutex lock
        
Solution 2 - O(N):
    - Store our vector 'nums' as a List of tuples (index, value). Key is index of non-zero element, Value is the element
    - Use two pointer on the two Lists
    
Follow-up: What if only one of the vectors is sparse?
Answer: Binary search on the non-sparse vector
    

Add-on concepts
1. Memory management
    1.1. Slab Allocator & Slab Class Sizes
        🔍 What is a Slab Allocator?
        A slab allocator is a memory management technique that pre-allocates chunks of memory (called slabs) for objects of the same size. It’s designed to:
        - Avoid fragmentation
        - Speed up allocation/deallocation
        - Reuse memory efficiently
        🧩 What Are Slab Class Sizes?
        - Slab classes are groups of slabs, each dedicated to a specific object size.
        - For example: one class for 64-byte objects, one for 128-byte objects, etc.
        - When you request memory, the allocator rounds your request up to the nearest slab class size.
        🧠 Example (like in Memcached):
        Slab Class Sizes: [64B, 128B, 256B, 512B, 1024B, ...]
        Request: 200B → Allocated from 256B slab class

        ✅ Pros:
        - Fast allocation
        - Low fragmentation
        - Great for fixed-size objects
        ❌ Cons:
        - Internal fragmentation (you get more than you asked for)
        - Not ideal for highly variable object sizes

    1.2. Buddy Allocator
        🔍 What Is It?
        - A buddy allocator is a memory allocation strategy that splits memory into blocks of size 2^k. When a block is freed, the allocator checks if its “buddy” (the adjacent block of the same size) is also free — if so, they’re merged.
        🧩 How It Works:
        - Start with a large block (e.g. 1024B).
        - If you need 128B, split the block recursively until you get 128B.
        - When freeing, check if the buddy block is also free → merge them.
        🧠 Example:
        Request: 128B
        Allocator splits: 1024 → 512 → 256 → 128
        Free: 128B → check buddy → merge back up

        ✅ Pros:
        - Efficient merging
        - Good for variable-size allocations
        - Avoids external fragmentation
        ❌ Cons:
        - Internal fragmentation (you may get more than needed)
        - Complexity in managing buddy trees

2. Concurrency
    2.1. Mutex Lock (Mutual Exclusion)
    - A mutex is a heavyweight lock.
    - When one thread acquires the lock, others must wait.
    - It’s managed by the OS and can put threads to sleep if they’re blocked.
    ✅ Pros:
    - Efficient for long critical sections
    - No CPU waste while waiting
    ❌ Cons:
    - Context switching overhead
    - Can cause contention and latency

    2.2. Spin Lock
    - A spin lock is a lightweight lock.
    - Threads spin in a loop (busy-wait) until the lock is available.
    - No sleeping — just burning CPU cycles.
    ✅ Pros:
    - Fast for short critical sections
    - No context switch overhead
    ❌ Cons:
    - Wastes CPU if held too long
    - Not ideal under high contention

    2.3. Hashmap Concurrency Strategies
    - Global lock: One mutex for the whole map (simple but slow).
    - Segmented locks: One lock per bucket or shard (better scalability).
    - Lock-free: Advanced techniques using atomic operations (e.g. Java’s ConcurrentHashMap).


"""

from typing import List
from collections import defaultdict

# Solution 1: HashMap
# O(N)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.mapping = {}                   # index -> value
        for i, num in enumerate(nums):
            if num != 0:
                self.mapping[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProduct = 0
        
        # Optimization: only care about indexes that already exist in our mapping
        # (instead of looping from 0 -> len(nums))
        for index, value in self.mapping.items():
            if index in vec.mapping:
                dotProduct += (value * vec.mapping[index])

        return dotProduct

        
# Solution 2: Two-pointer
# O(N)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.indexValueList = list()
        for i, num in enumerate(nums):
            if num != 0:
                self.indexValueList.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProduct = 0
        i, j = 0, 0
        while i < len(self.indexValueList) and j < len(vec.indexValueList):
            # Case 1: at a specific index, both vectors have non-zero value
            if self.indexValueList[i][0] == vec.indexValueList[j][0]:
                dotProduct += (self.indexValueList[i][1] * vec.indexValueList[j][1])
                i += 1
                j += 1
            elif self.indexValueList[i][0] < vec.indexValueList[j][0]:
                i += 1
            else: 
                j += 1
        
        return dotProduct
    

# Follow-up: What if only one of the vectors is sparse?
# Answer: Binary search
class SparseVector:
    def __init__(self, nums: List[int]):
        self.indexValueList = list()
        for i, num in enumerate(nums):
            if num != 0:
                self.indexValueList.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.indexValueList) < len(vec.indexValueList):
            return self.dotProductBinarySearchHelper(self, vec)
        
        return self.dotProductBinarySearchHelper(vec, self)
        
    def dotProductBinarySearchHelper(self, sparse: 'SparseVector', non_sparse: 'SparseVector') -> int:
        dotProduct = 0
        # ---------------------------------------------
        # Input: the desired vector_index in the sparse vector
        # Output: the index of pair (vector_index, value) in non_sparse.indexValueList. If no pair with desire vector_index, return -1
        def binarySearch(desiredVectorIndex) -> int:
            left, right = 0, len(non_sparse.indexValueList)-1
            while left <= right:
                mid = (right+left) // 2
                if non_sparse.indexValueList[mid][0] == desiredVectorIndex:
                    return mid
                
                if non_sparse.indexValueList[mid][0] < desiredVectorIndex:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1
        # ---------------------------------------------
        
        i = 0
        while i < len(sparse.indexValueList):
            sparse_index = sparse.indexValueList[i][0]
            j = binarySearch(sparse_index)

            if j != -1:
                dotProduct += sparse.indexValueList[i][1] * non_sparse.indexValueList[j][1]
            
            i += 1

        return dotProduct







if __name__ == "__main__":
    pass