/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table =========================================================

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
    int h = hashFunc(k); 
    // Keep looking until you find an available slot
    while(t[h] != NULL && t[h]->k != k){
        h = hashFunc(h+1); 
    }
    // If the slot is occupied but is has the same key, delete the old pair
    if (t[h] != NULL){
        delete t[h];
    }
    // Now the slot is definately available
    t[h] = new HashTableEntry(k, v); 
}


// Search a pair
int HashTable::searchKey(int k)
{
    int h = hashFunc(k); 
    // If the slot is not empty and the key k is different than k -> keep looking
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
    // Search for the slot
    while (t[h] != NULL){
        if (t[h]->k == k){
            break;
        } else {
            h = hashFunc(h+1); 
        }
    }
    // Found that slot
    if (t[h] == NULL) {
        std::cout << "No element found at key" << k << std::endl; 
        return;
    } else {
        delete t[h]; 
        std::cout << "Delete successfully" << k << std::endl; 
    }
};


// Print all pair of key-value
void HashTable::printTable()
{
    for (int i = 0; i < table_size; i++){
        std::cout << "Slot index: " << i << "       ";
        std::cout << "Key: " << t[i]->k << "  ";
        std::cout << "Value: " << t[i]->v << std::endl;
    }
}; 


int main() {
    HashTable hashTable_obj;
    hashTable_obj.insert(7788, 46);  
    hashTable_obj.printTable(); 

    #if 0
    int k, v;
    int c;
    while (1) {
        std::cout<<"1.Insert element into the table"<<std::endl;
        std::cout<<"2.Search element from the key"<<std::endl;
        std::cout<<"3.Delete element at a key"<<std::endl;
        std::cout<<"4.Exit"<<std::endl;
        std::cout<<"Enter your choice: ";
        std::cin>>c;
        switch(c) {
            case 1:
                std::cout<<"Enter element to be inserted: ";
                std::cin>>v;
                std::cout<<"Enter key at which element to be inserted: ";
                std::cin>>k;
                hashTable_obj.insert(k, v);
            break;
            case 2:
                std::cout<<"Enter key of the element to be searched: ";
                std::cin>>k;
                if (hashTable_obj.searchKey(k) == -1) {
                    std::cout<<"No element found at key "<<k<<std::endl;
                    continue;
                } else {
                    std::cout<<"Element at key "<<k<<" : ";
                    std::cout<<hashTable_obj.searchKey(k)<<std::endl;
                }
            break;
            case 3:
                std::cout<<"Enter key of the element to be deleted: ";
                std::cin>>k;
                hashTable_obj.remove(k);
            break;
            case 4:
                exit(1);
            default:
                std::cout<<"\nEnter correct option\n";
        }
    }
    #endif





    return 0;
}
