class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        
        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]
            
            product = val1 * val2
            min_freq = min(freq1, freq2)
            
            if res and res[-1][0] == product:
                res[-1][1] += min_freq
            else:
                res.append([product, min_freq])
            
            encoded1[i][1] -= min_freq
            encoded2[j][1] -= min_freq
            
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        
        return res