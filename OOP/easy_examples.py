"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

In no way, shape or form am I intending to infringe rights of the copyright holder. Content used is strictly for 
reviewing purposes. 
https://realpython.com/python3-object-oriented-programming/

========================================= Examples for Object Oriented Programming =========================================
"""

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # dunder method to get a friendlier output when print object
    def __str__(self):
        return f"{self.name} wants to say something"

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


if __name__ == "__main__":
    miles = Dog("Miles", 5)
    print(miles)
    print(miles.description())
    print(miles.speak("I love you"))

