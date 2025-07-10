"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table =========================================================
Hash tables are a type of data structure in which the address or the index value of the data element is generated 
from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. 
In other words Hash table stores key-value pairs but the key is generated through a hashing function.

So the search and insertion function of a data element becomes much faster as the key values themselves become the
index of the array which stores the data.

🧠 Key Concepts Preserved
- Each bucket is a linked list of key-value pairs.
- Handles collisions via separate chaining.
- Supports insert, search, remove, and print operations.

"""

TABLE_SIZE_SC = 10

# Same as a LinkedList node
class HashTableEntry:
    def __init__(self, key: int, value: int):
        self.k = key
        self.v = value
        self.next = None


class HashTableSeparateChaining:
    def __init__(self):
        # Initialize table with empty slots (None)
        self.t = [None for _ in range(TABLE_SIZE_SC)]

    def hash_func(self, key: int) -> int:
        return key % TABLE_SIZE_SC

    def insert(self, key: int, value: int) -> None:
        h = self.hash_func(key)

        if self.t[h] is None:
            self.t[h] = HashTableEntry(key, value)
        else:
            temp = self.t[h]
            prev = None

            # Search for duplicate key
            while temp:
                if temp.k == key:
                    temp.v = value  # Update existing key
                    return
                prev = temp
                temp = temp.next

            # Append new node at the end
            prev.next = HashTableEntry(key, value)

    def search_key(self, key: int) -> int:
        h = self.hash_func(key)
        temp = self.t[h]

        while temp and temp.k != key:
            temp = temp.next

        return temp.v if temp else -1

    def remove(self, key: int) -> None:
        h = self.hash_func(key)
        temp = self.t[h]
        prev = None

        if not temp:
            return  # Nothing to remove

        while temp and temp.k != key:
            prev = temp
            temp = temp.next

        if not temp:
            return  # Key not found

        if not prev:
            # Remove head node
            self.t[h] = temp.next
        else:
            # Remove middle or tail node
            prev.next = temp.next

    def print_table(self) -> None:
        for i in range(TABLE_SIZE_SC):
            print(f"Slot index: {i}       ", end="")
            if self.t[i] is None:
                print("NULL")
            else:
                temp = self.t[i]
                while temp:
                    print(f"Key: {temp.k} -- Value: {temp.v} ---> ", end="")
                    temp = temp.next
                print("NULL")







