"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Implement LRU and LFU =========================================================

1. Leetcode 208. Implement Trie (Prefix Tree)     
2. Leetcode 588. Design In-Memory File System

"""

import collections
from typing import List

# Leetcode 208. Implement Trie (Prefix Tree) ------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        lastChar = word[-1]

        # iterate each char in word
        for char in word:
            # a char node exists as child
            if char in current.children:
                current = current.children[char]
            # add new char node
            else:
                newNode = TrieNode()
                current.children[char] = newNode
                current = newNode

        # mark the last char node as end of a word if needed
        if char == lastChar:
            current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root

        for i in range (len(word)):
            char = word[i]
            # if char is not one of the children -> not found
            if char not in current.children:
                return False
            # if char is on of the children
            else:
                current = current.children[char]
                if i == len(word)-1 and current.isEnd: # only return True if the last char Node has isEnd == True
                    return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        
        return True
    

# Leetcode 588. Design In-Memory File System ------------------------------------------------------------------------------
class TrieNode588:
    def __init__(self):
        # Set of children paths
        self.children = set()                           # (Only available for Dirs)
        self.content = ""                               # (Only available for Files)
        self.isFile = False

class FileSystem:
    def __init__(self):
        self.root = TrieNode588()                          
        self.pathToTrieNode = collections.defaultdict(TrieNode588)     
        self.pathToTrieNode['/'] = self.root           # root dir will have name as '/' in the mapping

    def ls(self, path: str) -> List[str]:
        # carefully prepare the targetName, which is the name of the file or dir
        targetName = None
        if path == "/": 
            targetName = path
        else: 
            targetName = path.split("/")[-1]                
        
        # retrive the node from the path, NOT the targetName            
        targetNode = self.pathToTrieNode[path]          

        # Case 1: It's a file path
        if targetNode.isFile:
            return [targetName]

        # Case 2: It's a dir path
        result = []
        for child in targetNode.children:
            childName = child.split("/")[-1]
            result.append(childName)
        # print(result)

        return sorted(result)   # return in lexicographic order

    def mkdir(self, path: str) -> None:
        current = self.root
        pathList = path.split("/")      # min len() == 2
        pathBuilder = ""

        # iterate each dir name in the path
        for d in pathList:
            # node for root dir is already created in the constructor, so skipping root dir
            if d == '':
                continue

            pathBuilder += "/{}".format(d)
            print(pathBuilder)

            # Case 1. dir already exists
            if pathBuilder in self.pathToTrieNode:              
                dNode = self.pathToTrieNode[pathBuilder]        # retrive node
                current = dNode
            # Case 2. dir not exists yet
            else:                
                dNode = TrieNode588()
                self.pathToTrieNode[pathBuilder] = dNode        # add to global mapping
                current.children.add(pathBuilder)               # add d as a new child of current
                current = dNode

        # debug
        # for d in pathList:
        #     dNode = self.nameToTrieNode[d]
        #     print("{} - {}".format(d, dNode.children))

    def addContentToFile(self, filePath: str, content: str) -> None:        
        # Case 1: If file already exists
        if filePath in self.pathToTrieNode:
            fileNode = self.pathToTrieNode[filePath]
            if fileNode.isFile:
                fileNode.content += content
                return
        
        # Case 2: File does not exist yet
        self.mkdir(filePath)                            # create the file and its dir   
        fileNode = self.pathToTrieNode[filePath]        # retrive the fileNode
        fileNode.isFile = True                          # mark the node as a file
        fileNode.content += content

    def readContentFromFile(self, filePath: str) -> str:
        fileNode = self.pathToTrieNode[filePath]

        return fileNode.content





if __name__ == "__main__":
    # Tries
    """
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")
    trie.search("app")
    trie.search("applepie")
    """

    # File System 
    fs = FileSystem()
    fs.ls("/")
    fs.mkdir("/a/b/c")
    fs.mkdir("/a/b")
    fs.ls("/a/b")
    fs.mkdir("/a/b/a")
    fs.ls("/a/b")

    fs.addContentToFile("/a/b/c/d", "hello" )
    fs.readContentFromFile("a/b/c/d")









