class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> result;
        int m = nums1.size(), n = nums2.size();
        for (int i = max(0, k - n); i <= min(k, m); ++i) {
            vector<int> candidate = merge(maxArray(nums1, i), maxArray(nums2, k - i), k);
            if (candidate > result) result = candidate;
        }
        return result;
    }
    
private:
    vector<int> maxArray(vector<int>& nums, int k) {
        vector<int> maxArr(k, 0);
        int drop = nums.size() - k;
        for (int i = 0, j = 0; i < nums.size(); ++i) {
            while (j > 0 && maxArr[j - 1] < nums[i] && drop > 0) {
                j--;
                drop--;
            }
            if (j < k) {
                maxArr[j++] = nums[i];
            } else {
                drop--;
            }
        }
        return maxArr;
    }

    vector<int> merge(vector<int> nums1, vector<int> nums2, int k) {
        vector<int> merged(k, 0);
        int i = 0, j = 0, r = 0;
        while (r < k) {
            if (greater(nums1, i, nums2, j)) 
                merged[r++] = nums1[i++];
            else 
                merged[r++] = nums2[j++];
        }
        return merged;
    }

    bool greater(vector<int>& nums1, int i, vector<int>& nums2, int j) {
        while (i < nums1.size() && j < nums2.size() && nums1[i] == nums2[j]) {
            ++i;
            ++j;
        }
        return j == nums2.size() || (i < nums1.size() && nums1[i] > nums2[j]);
    }
};