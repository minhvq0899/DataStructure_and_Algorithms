/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table with Seperate Chaining =========================================================

*/ 
    
// #pragma once

#ifndef HASHTABLE_SEPARATE_CHAINING_H
#define HASHTABLE_SEPARATE_CHAINING_H

#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>

const int table_size_sc = 10; 

class HashTableEntry_SeparateChaining
{
public:
    int k; 
    int v; 
    HashTableEntry_SeparateChaining* next; 

    // constructor
    HashTableEntry_SeparateChaining(int k, int v){
        this->k = k;
        this->v = v; 
        this->next = nullptr; 
    };
}; 


class HashTable_SeparateChaining
{
private: 
    HashTableEntry_SeparateChaining** t; // an aray of pointers point to a HashTableEntry_SeparateChaining

public:
    HashTable_SeparateChaining();
    ~HashTable_SeparateChaining();

    int hashFunc(int k); 
    void insert(int k, int v); 
    int searchKey(int k); 
    void remove(int k);
    void printTable();
};

#endif














