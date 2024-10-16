#include <vector>
using namespace std;

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        return mergeSortAndCount(nums, 0, nums.size() - 1);
    }
    
private:
    int mergeSortAndCount(vector<int>& nums, int left, int right) {
        if (left >= right) return 0;

        int mid = left + (right - left) / 2;
        int count = mergeSortAndCount(nums, left, mid) + mergeSortAndCount(nums, mid + 1, right);
        
        int j = mid + 1;
        for (int i = left; i <= mid; ++i) {
            while (j <= right && nums[i] > 2LL * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }

        merge(nums, left, mid, right);
        return count;
    }

    void merge(vector<int>& nums, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        vector<int> leftArr(n1), rightArr(n2);

        for (int i = 0; i < n1; ++i) {
            leftArr[i] = nums[left + i];
        }
        for (int i = 0; i < n2; ++i) {
            rightArr[i] = nums[mid + 1 + i];
        }

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (leftArr[i] <= rightArr[j]) {
                nums[k++] = leftArr[i++];
            } else {
                nums[k++] = rightArr[j++];
            }
        }

        while (i < n1) {
            nums[k++] = leftArr[i++];
        }

        while (j < n2) {
            nums[k++] = rightArr[j++];
        }
    }
};