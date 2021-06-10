/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table with Seperate Chaining =========================================================



*/ 
    
#include "hashtable_separate_chaining.h" 

// Constructor for a new Hash Table with seperate chaining
HashTable_SeparateChaining::HashTable_SeparateChaining() 
{
    this->t = new HashTableEntry_SeparateChaining * [table_size_sc]; // an array of pointers 
    for (int i = 0; i < table_size_sc; i++) {
        t[i] = NULL; 
    }
};


// Destructor for a new Hash Table
HashTable_SeparateChaining::~HashTable_SeparateChaining()
{
    for (int i = 0; i < table_size_sc; i++){
        delete t[i]; 
    }
    delete[] t; 
}; 


// Hash Function
int HashTable_SeparateChaining::hashFunc(int key)
{
    return key % table_size_sc; 
};


/** Insert new pair of key-value 
Move to the bucket corresponds to the above calculated hash index and sequentially search for a possible duplicate key.  
If there is none then insert the new node at the end of the list.
*/
void HashTable_SeparateChaining::insert(int key, int val)
{
    int h = hashFunc(key); 

    if (t[h] == NULL) {
        t[h] = new HashTableEntry_SeparateChaining(key, val); 
    } else {
        HashTableEntry_SeparateChaining* temp = t[h]; 
        HashTableEntry_SeparateChaining* prev = nullptr; 
        //sequentially search for possible duplicate key
        while (temp != NULL){
            if (temp->k == key){
                temp->v = val; 
                return; 
            }
            prev = temp; 
            temp = temp->next; 
        }
        // we reach the end of the linked list
        prev->next = new HashTableEntry_SeparateChaining(key, val); 
    }
}


// Search a pair
int HashTable_SeparateChaining::searchKey(int key)
{
    int h = hashFunc(key);

    HashTableEntry_SeparateChaining* temp = t[h]; 
    while (temp && temp->k != key) {
        temp = temp->next; 
    }

    if (!temp) return -1;
    else return temp->v; 
}


// Remove a pair
void HashTable_SeparateChaining::remove(int key)
{
    int h = hashFunc(key); 
    
    HashTableEntry_SeparateChaining* prev = nullptr; 
    HashTableEntry_SeparateChaining* temp = t[h]; 

    // special case: t[h] is NULL
    if (!temp) {
        return;
    } 

    // search for desired key
    while (temp && temp->k != key) {
        prev = temp;
        temp = temp->next; 
    }

    if (!temp) {                        // cannot find the desired key
        return; 
    } else {
        if (!temp->next && !prev) {     // special case 1: when t[h] only has 1 node and it has the desired key
            t[h] = NULL; 
        } else {    
            if (!prev) {                // special case 2: when remove the head of a long list
                t[h] = temp->next; 
            } else {                    // normal case: remove a node in the middle of the list
                prev->next = temp->next; 
            }
        }

        delete temp; 
    }
};



// Print all pair of key-value
void HashTable_SeparateChaining::printTable()
{
    for (int i = 0; i < table_size_sc; i++){
        std::cout << "Slot index: " << i << "       ";
        if (t[i] == NULL) {
            std::cout << "NULL" << std::endl; 
        } else {
            HashTableEntry_SeparateChaining* temp = t[i]; 
            while (temp != NULL){    
                std::cout << "Key: " << temp->k << " -- ";
                std::cout << "Value: " << temp->v << " ---> ";
                temp = temp->next; 
            }
            std::cout << "NULL\n"; 
        }
    }
}; 


