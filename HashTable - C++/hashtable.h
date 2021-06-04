/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table =========================================================

*/ 
    
#pragma once

#include<iostream>
#include<cstdlib>
#include<string>
#include<cstdio>

const int table_size = 20; 

class HashTableEntry 
{​​​​​​​
public:
    int k; 
    int v; 
    HashTableEntry(int k, int v);
}​​​​​​​;


class HashTable
{​​​​​​​
private:
    HashTableEntry** t; // an aray of pointers point to a HashTableEntry
public:
    HashTable(); 
    ~HashTable(); 


    int hashFunc(int k); 
    void insert(int k, int v); 
    int searchKey(int k); 
    void remove(int k);
    void printTable();
}​​​​​​​;













