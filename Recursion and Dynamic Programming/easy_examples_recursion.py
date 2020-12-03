"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

In no way, shape or form am I intending to infringe rights of the copyright holder. Content used is strictly for 
reviewing purposes. 

========================================= Examples for Recursion and Dynamic Programming =========================================
"""

# convert decimal number to binary using recursive function
def IntToBinary(N):
    if N == 1: return "1"  # base case
    return IntToBinary(N // 2) + str(N  % 2)

# Fibonacci numbers
def fibonacci(n):
    if n > 30: print("It will take minutes to compute. I am too lazy")
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    # Int -> Binary
    binary_string = IntToBinary(26)
    print("The binary representation of 26 is: ", binary_string)

    # fibonacci
    print("Fibonacci 13 is ", fibonacci(13))


