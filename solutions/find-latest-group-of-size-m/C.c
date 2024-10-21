#include <stdlib.h>

// Function to find the root of a set with path compression
int find_root(int* parent, int x) {
    if (parent[x] != x) {
        parent[x] = find_root(parent, parent[x]);
    }
    return parent[x];
}

// Function to perform union of two sets
void union_sets(int* parent, int* size, int x, int y, int m, int* count_m) {
    int root_x = find_root(parent, x);
    int root_y = find_root(parent, y);
    
    if (root_x == root_y) return; // Already in the same set
    
    // If either set has size m, decrement count_m
    if (size[root_x] == m) (*count_m)--;
    if (size[root_y] == m) (*count_m)--;
    
    // Merge smaller set into larger set
    if (size[root_x] < size[root_y]) {
        parent[root_x] = root_y;
        size[root_y] += size[root_x];
        
        // If new set has size m, increment count_m
        if (size[root_y] == m) (*count_m)++;
    }
    else {
        parent[root_y] = root_x;
        size[root_x] += size[root_y];
        
        // If new set has size m, increment count_m
        if (size[root_x] == m) (*count_m)++;
    }
}

int findLatestStep(int* arr, int arrSize, int m){
    // Initialize Union-Find structures
    // +2 to handle edge cases for positions 0 and n+1
    int n = arrSize;
    int* parent = (int*)malloc((n + 2) * sizeof(int));
    int* size = (int*)calloc((n + 2), sizeof(int)); // Initialized to 0
    
    for (int i = 0; i <= n +1; i++) {
        parent[i] = i;
    }
    
    int count_m = 0;
    int latest_step = -1;
    
    for (int step =1; step <= n; step++) {
        int pos = arr[step -1];
        size[pos] =1; // Flip the bit to 1
        
        // Initially, this new 1 forms a group of size 1
        if (m ==1) count_m++;
        
        // Check left neighbor
        if (pos >1 && size[pos -1] >0) {
            // If the left group was of size m, decrement count_m
            if (size[find_root(parent, pos -1)] == m) count_m--;
            // Merge current pos with left neighbor
            union_sets(parent, size, pos, pos -1, m, &count_m);
        }
        
        // Check right neighbor
        if (pos < n && size[pos +1] >0) {
            // If the right group was of size m, decrement count_m
            if (size[find_root(parent, pos +1)] == m) count_m--;
            // Merge current pos with right neighbor
            union_sets(parent, size, pos, pos +1, m, &count_m);
        }
        
        // After potential merges, check if the current group has size m
        int root = find_root(parent, pos);
        if (size[root] == m) {
            count_m++;
        }
        
        // Update latest_step if there's at least one group of size m
        if (count_m >0) {
            latest_step = step;
        }
    }
    
    free(parent);
    free(size);
    return latest_step;
}