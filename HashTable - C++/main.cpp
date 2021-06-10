#include "hashtable.h"
#include "hashtable_separate_chaining.h" 

void main_hashtable(){
    HashTable hashTable_obj;
    int k, v;
    int s; 
    int c;
    while (1) {
        std::cout<<"1.Insert element into the table"<<std::endl;
        std::cout<<"2.Search element from the key"<<std::endl;
        std::cout<<"3.Delete element at a key"<<std::endl;
        std::cout<<"4.Print table"<<std::endl;
        std::cout<<"5.Exit"<<std::endl;
        std::cout<<"Enter your choice: ";
        std::cin>>c;
        switch(c) {
            case 1:
                std::cout<<"Enter element to be inserted: ";
                std::cin>>v;
                std::cout<<"Enter key at which element to be inserted: ";
                std::cin>>k;
                hashTable_obj.insert(k, v);
                std::cout << "\n";
            break;
            case 2:
                std::cout<<"Enter key of the element to be searched: ";
                std::cin>>k;
                s = hashTable_obj.searchKey(k); 
                if (s == -1) {
                    std::cout<<"No element found at key "<< k << "\n" << std::endl;
                    continue;
                } else {
                    std::cout<<"Element at key "<<k<<" : ";
                    std::cout<< s << "\n" << std::endl;
                }
            break;
            case 3:
                std::cout<<"Enter key of the element to be deleted: ";
                std::cin>>k;
                hashTable_obj.remove(k);
                std::cout << "\n"; 
            break;
            case 4:
                hashTable_obj.printTable();
                std::cout << "\n"; 
            break;
            case 5:
                exit(1);
            default:
                std::cout<<"\nEnter correct option\n";
        }
    }
};


void main_hashtable_separatechaining(){
    HashTable_SeparateChaining hashTable_sc_obj;
    int k, v;
    int s; 
    int c;
    while (1) {
        std::cout<<"1.Insert element into the table"<<std::endl;
        std::cout<<"2.Search element from the key"<<std::endl;
        std::cout<<"3.Delete element at a key"<<std::endl;
        std::cout<<"4.Print table"<<std::endl;
        std::cout<<"5.Exit"<<std::endl;
        std::cout<<"Enter your choice: ";
        std::cin>>c;
        switch(c) {
            case 1:
                std::cout<<"Enter element to be inserted: ";
                std::cin>>v;
                std::cout<<"Enter key at which element to be inserted: ";
                std::cin>>k;
                hashTable_sc_obj.insert(k, v);
                std::cout << "\n";
            break;
            case 2:
                std::cout<<"Enter key of the element to be searched: ";
                std::cin>>k;
                s = hashTable_sc_obj.searchKey(k); 
                if (s == -1) {
                    std::cout<<"No element found at key "<< k << "\n" << std::endl;
                    continue;
                } else {
                    std::cout<<"Element at key "<<k<<" : ";
                    std::cout<< s << "\n" << std::endl;
                }
            break;
            case 3:
                std::cout<<"Enter key of the element to be deleted: ";
                std::cin>>k;
                hashTable_sc_obj.remove(k);
                std::cout << "\n"; 
            break;
            case 4:
                hashTable_sc_obj.printTable();
                std::cout << "\n"; 
            break;
            case 5:
                exit(1);
            default:
                std::cout<<"\nEnter correct option\n";
        }
    }
}; 


int main() {
    // test for hash table
    main_hashtable(); 

    // test for hash table with separate   
    main_hashtable_separatechaining(); 

    // Debug
    // HashTable_SeparateChaining hashTable_sc_obj;
    // hashTable_sc_obj.insert(6688, 46);
    // hashTable_sc_obj.insert(7788, 48);
    // hashTable_sc_obj.printTable();

    return 0;
}

