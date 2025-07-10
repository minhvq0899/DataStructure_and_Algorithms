"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Implement LRU and LFU =========================================================



"""

import collections
from typing import List
from threading import Thread, Lock
from queue import Queue
from typing import List

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Extract the hostname from the start URL
        def get_hostname(url: str) -> str:
            return url.split("/")[2]  # e.g., "http://news.yahoo.com" → "news.yahoo.com"

        hostname = get_hostname(startUrl)

        visited = set()         # To track visited URLs
        visited_lock = Lock()   # Lock to protect access to the visited set

        q = Queue()
        q.put(startUrl)

        # ---------------------------------------------------
        def worker():
            while True:
                try:
                    url = q.get(timeout=1)  # Wait for a URL to crawl
                except:
                    return  # Exit thread if queue is empty for too long

                # Get all URLs from the current page
                for next_url in htmlParser.getUrls(url):
                    if get_hostname(next_url) != hostname:
                        continue  # Skip URLs from different hostnames

                    with visited_lock:
                        if next_url in visited:
                            continue
                        visited.add(next_url)
                        q.put(next_url)

                q.task_done()
        # ---------------------------------------------------
        
        # Initialize visited with the start URL
        with visited_lock:
            visited.add(startUrl)

        # Start multiple threads
        threads = []
        for _ in range(8):  # You can tune the number of threads
            t = Thread(target=worker)
            t.start()
            threads.append(t)

        q.join()  # Wait until all URLs are processed

        return list(visited)



if __name__ == "__main__":







