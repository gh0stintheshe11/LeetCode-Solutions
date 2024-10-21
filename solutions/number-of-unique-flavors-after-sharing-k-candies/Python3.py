class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        rem = dict()
        for c in candies[k:]:
            if c in rem:
                rem[c] += 1
            else:
                rem[c] = 1
        
        m = len(rem)
        
        for i in range(0, len(candies) - k):
            if candies[i] in rem:
                rem[candies[i]] += 1
            else:
                rem[candies[i]] = 1

            rem[candies[i + k]] -= 1
            
            if rem[candies[i + k]] == 0:
                del rem[candies[i + k]]

            m = max(m, len(rem))

        return m