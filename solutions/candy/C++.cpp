class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        
        if(n <= 1)
            return n;
        
        vector<int> candies(n, 1);
        
        // Left to right; ensuring right child gets more candies if they have a higher rating
        for(int i = 1; i < n; ++i) {
            if(ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        
        // Right to left; ensuring left child gets more candies if they have a higher rating
        for(int i = n - 2; i >= 0; --i) {
            if(ratings[i] > ratings[i + 1]) {
                candies[i] = max(candies[i], candies[i + 1] + 1);
            }
        }
        
        // Sum up the candies
        int totalCandies = 0;
        for(int candy : candies) {
            totalCandies += candy;
        }
        
        return totalCandies;
    }
};