"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

In no way, shape or form am I intending to infringe rights of the copyright holder. Content used is strictly for 
reviewing purposes. 
https://www.dataquest.io/blog/python-api-tutorial/

========================================= Usage of APIs =========================================
"""


import requests
import json
"""
json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
"""

response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code)
# print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())



