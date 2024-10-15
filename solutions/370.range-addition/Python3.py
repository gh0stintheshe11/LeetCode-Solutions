class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length
        
        for start, end, inc in updates:
            result[start] += inc
            if end + 1 < length:
                result[end + 1] -= inc
        
        cur_sum = 0
        for i in range(length):
            cur_sum += result[i]
            result[i] = cur_sum
        
        return result