/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table =========================================================
class HashTable
{
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
};
*/ 
    
#include "hashtable.h"

// Constructor for a slot
HashTableEntry::HashTableEntry(int k, int v)
{
    this->k = k; 
    this->v = v; 
}; 


// Constructor for a new Hash Table
HashTable::HashTable() 
{
    this->t = new HashTableEntry * [table_size]; // an array of pointers 
    for (int i = 0; i < table_size; i++) {
        t[i] = NULL; 
    }
};


// Destructor for a new Hash Table
HashTable::~HashTable()
{
    for (int i = 0; i < table_size; i++){
        delete t[i]; 
    }
    delete[] t; 
}; 


// Hash Function
int HashTable::hashFunc(int k)
{
    return k % table_size; 
};


// Insert new pair of key-value
void HashTable::insert(int k, int v)
{
    int cap = 0; 

    int h = hashFunc(k); 
    // If the slot is occupied AND it has different key
    while(t[h] != NULL && t[h]->k != k){
        cap++; 
        if (cap >= table_size){
            std::cout << "The hash table is full" << std::endl; 
            return; 
        } else {
            h = hashFunc(h+1); 
        }
    }
    // If the slot is occupied BUT is has the same key, delete the old pair
    if (t[h] != NULL) { // && t[h]->k == k
        delete t[h];
    }
    // Now the slot is definately available
    t[h] = new HashTableEntry(k, v); 
}


// Search a pair
int HashTable::searchKey(int k)
{
    int h = hashFunc(k); 
    // If the slot is occupied AND it has different key -> keep looking
    while (t[h] != NULL && t[h]->k != k){
        h = hashFunc(h+1);
    }
    // If we found the slot but it's empty
    if (t[h] == NULL){
        return -1; 
    } else {
        return t[h]->v; 
    }
}


// Remove a pair
void HashTable::remove(int k)
{
    int h = hashFunc(k); 
    // If the slot is occupied AND it has different key
    while (t[h] != NULL && t[h]->k != k){
        h = hashFunc(h+1); 
    }

    // Found that slot
    if (t[h] == NULL) {
        std::cout << "No element found at key " << k << std::endl; 
        return;
    } else {
        delete t[h]; 
        t[h] = NULL;  
        std::cout << "Delete successfully " << k << std::endl; 
    }
};


// Print all pair of key-value
void HashTable::printTable()
{
    for (int i = 0; i < table_size; i++){
        std::cout << "Slot index: " << i << "       ";
        if (t[i] == NULL) {
            std::cout << "NULL" << std::endl; 
        } else {
            std::cout << "Key: " << t[i]->k << " ---> ";
            std::cout << "Value: " << t[i]->v << std::endl;
        }
    }
}; 

