class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        store_2 = Counter(word2)
        store_1 = defaultdict(int)
        l, r = 0, 0
        res = 0
        size = 0
        while r < n:
            store_1[word1[r]] += 1

            if store_1[word1[r]] <= store_2[word1[r]]:
                size += 1  
            
            while size == m and l <= r:
                res += (n - r)
                store_1[word1[l]] -= 1
                if word1[l] in store_2 and store_1[word1[l]] < store_2[word1[l]]:
                    size -= 1
                l += 1
            
            r += 1

        return res