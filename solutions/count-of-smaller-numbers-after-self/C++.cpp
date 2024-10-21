#include <vector>
#include <utility>
#include <algorithm>

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 0);
        vector<pair<int, int>> pairs(n);
        
        for (int i = 0; i < n; ++i) {
            pairs[i] = {nums[i], i};
        }
        
        mergeSort(pairs, 0, n, result);
        return result;
    }
    
private:
    void mergeSort(vector<pair<int, int>>& pairs, int left, int right, vector<int>& result) {
        if (right - left <= 1) return;
        
        int mid = left + (right - left) / 2;
        mergeSort(pairs, left, mid, result);
        mergeSort(pairs, mid, right, result);
        
        merge(pairs, left, mid, right, result);
    }
    
    void merge(vector<pair<int, int>>& pairs, int left, int mid, int right, vector<int>& result) {
        vector<pair<int, int>> temp(right - left);
        int i = left, j = mid, k = 0;
        
        while (i < mid && j < right) {
            if (pairs[i].first <= pairs[j].first) {
                temp[k++] = pairs[j++];
            } else {
                result[pairs[i].second] += right - j;
                temp[k++] = pairs[i++];
            }
        }
        
        while (i < mid) {
            temp[k++] = pairs[i++];
        }
        
        while (j < right) {
            temp[k++] = pairs[j++];
        }
        
        for (int i = left; i < right; ++i) {
            pairs[i] = temp[i - left];
        }
    }
};