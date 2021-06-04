/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table =========================================================

*/ 
    
#include "HashTable.h"

HashTableEntry::HashTableEntry(int k, int v) {​​​​​​​
    this->k = k;
    this->v = v;
}​​​​​​​; 

// Constructor
HashTable::HashTable() {​​​​​​​
    t = new HashTableEntry * [table_size]; // using pointer to pointer
    for (int i = 0; i < table_size; i++) {​​​​​​​
        t[i] = NULL; 
    }​​​​​​​
}​​​​​​​; 


// Destructor
HashTable::~HashTable() {​​​​​​​
    for (int i = 0; i < table_size; i++) {​​​​​​​
        if (t[i]) {​​​​​​​
            delete t[i]; 
        }​​​​​​​
    }​​​​​​​
    delete[] t; 
}​​​​​​​; 


// Hash Function
int HashTable::hashFunc(int k) {​​​​​​​
    return k % table_size; 
}​​​​​​​;


// Insert new pair of key-value
void HashTable::insert(int k, int v) {​​​​​​​
    int h = hashFunc(k); 
    // Keep looking until you find an available slot
    while (t[h] != NULL && t[h]->k != k) {​​​​​​​
        h = hashFunc(h + 1); 
    }​​​​​​​
    // If the slot is occupied but is has the same key, delete the old pair
    if (t[h] != NULL) {​​​​​​​
        delete t[h]; 
    }​​​​​​​
    // Now the slot is definately available
    t[h] = new HashTableEntry(k, v); 
}​​​​​​​;


// Search a pair
int HashTable::searchKey(int k) {​​​​​​​
    int h = hashFunc(k); 
    // If the slot is occupied and occupied by a different pair -> keep looking
    while (t[h] != NULL && t[h]->k != k) {​​​​​​​
        h = hashFunc(h + 1);
    }​​​​​​​
    // Found the potential slot
    if (t[h] == NULL) {​​​​​​​
        return -1;
    }​​​​​​​
    else {​​​​​​​
        return t[h]->v; 
    }​​​​​​​
}​​​​​​​;


// Remove a pair
void HashTable::remove(int k) {​​​​​​​
    int h = hashFunc(k); 
    // search for that slot
    while (t[h] != NULL) {​​​​​​​
        if (t[h]->k == k) {​​​​​​​
            break; 
        }​​​​​​​
        h = hashFunc(h + 1); 
    }​​​​​​​
    // Found that slot
    if (t[h] == NULL) {​​​​​​​
        std::cout << "No element found at key" << k << std::endl; 
    }​​​​​​​
    else {​​​​​​​
        delete t[h]; 
        std::cout << "Element deleted successfully" << std::endl; 
    }​​​​​​​
}​​​​​​​;


void HashTable::printTable() {​​​​​​​
    std::cout << "Slot Index:";
    for (int i = 0; i < table_size; i++) {​​​​​​​
        std::cout << "    " << i; 
    }​​​​​​​
    std::cout << "\nKey:       ";
    for (int i = 0; i < table_size; i++) {​​​​​​​
        if (t[i]) {​​​​​​​
            
        }​​​​​​​
    }​​​​​​​


}​​​​​​​; 


int main() {​​​​​​​
    
}​​​​​​​


















