#include <stdlib.h>

/**
 * Hash table entry structure
 */
typedef struct HashEntry {
    int key;            // The number from the array
    int value;          // The index of the number
    struct HashEntry* next;  // Pointer to the next entry (for chaining in case of collisions)
} HashEntry;

/**
 * Hash table structure
 */
typedef struct HashTable {
    int size;           // Size of the hash table array
    HashEntry** table;  // Array of pointers to HashEntry
} HashTable;

/**
 * Creates a new hash table
 */
HashTable* createHashTable(int size) {
    HashTable* ht = (HashTable*)malloc(sizeof(HashTable));
    ht->size = size;
    ht->table = (HashEntry**)malloc(sizeof(HashEntry*) * size);
    for (int i = 0; i < size; i++)
        ht->table[i] = NULL;
    return ht;
}

/**
 * Simple hash function
 */
int hashFunction(HashTable* ht, int key) {
    // Use modulo operator to stay within the table size
    // To handle negative keys, make sure the result is non-negative
    return abs(key) % ht->size;
}

/**
 * Inserts a key-value pair into the hash table
 */
void insertHashTable(HashTable* ht, int key, int value) {
    int hashIndex = hashFunction(ht, key);
    HashEntry* newEntry = (HashEntry*)malloc(sizeof(HashEntry));
    newEntry->key = key;
    newEntry->value = value;
    newEntry->next = ht->table[hashIndex];
    ht->table[hashIndex] = newEntry;
}

/**
 * Searches for a key in the hash table and returns its associated value
 * Returns -1 if the key is not found
 */
int searchHashTable(HashTable* ht, int key) {
    int hashIndex = hashFunction(ht, key);
    HashEntry* entry = ht->table[hashIndex];
    while (entry != NULL) {
        if (entry->key == key)
            return entry->value;
        entry = entry->next;
    }
    return -1;  // Key not found
}

/**
 * Frees the memory allocated for the hash table
 */
void freeHashTable(HashTable* ht) {
    for (int i = 0; i < ht->size; i++) {
        HashEntry* entry = ht->table[i];
        while (entry != NULL) {
            HashEntry* temp = entry;
            entry = entry->next;
            free(temp);
        }
    }
    free(ht->table);
    free(ht);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Initialize the hash table
    // Choosing a prime number greater than numsSize for better distribution
    HashTable* ht = createHashTable(2 * numsSize + 1);

    // Allocate memory for the result array
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 0;

    // Traverse the array
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];

        // Check if the complement exists in the hash table
        int index = searchHashTable(ht, complement);
        if (index != -1) {
            // Complement found, return the indices
            result[0] = index;
            result[1] = i;
            *returnSize = 2;
            freeHashTable(ht);  // Free the hash table before returning
            return result;
        }

        // Insert the current number and its index into the hash table
        insertHashTable(ht, nums[i], i);
    }

    // If no solution is found (should not happen per problem constraints)
    free(result);
    *returnSize = 0;
    freeHashTable(ht);
    return NULL;
}
