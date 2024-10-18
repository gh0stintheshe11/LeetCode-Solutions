class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        
        return result