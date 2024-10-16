#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        if (n == 0) return 0;

        vector<long> sums(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            sums[i + 1] = sums[i] + nums[i];
        }

        return countWhileMergeSort(sums, 0, n + 1, lower, upper);
    }

private:
    int countWhileMergeSort(vector<long>& sums, int start, int end, int lower, int upper) {
        if (end - start <= 1) return 0;
        int mid = start + (end - start) / 2;
        int count = countWhileMergeSort(sums, start, mid, lower, upper) +
                    countWhileMergeSort(sums, mid, end, lower, upper);

        int j = mid, k = mid, t = mid;
        vector<long> cache(end - start, 0);
        for (int i = start, r = 0; i < mid; ++i, ++r) {
            while (k < end && sums[k] - sums[i] < lower) k++;
            while (j < end && sums[j] - sums[i] <= upper) j++;
            while (t < end && sums[t] < sums[i]) cache[r++] = sums[t++];
            cache[r] = sums[i];
            count += j - k;
        }
        copy(cache.begin(), cache.begin() + (t - start), sums.begin() + start);
        return count;
    }
};