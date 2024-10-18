class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(nums)) : 
            heappush(heap, (nums[i], i))

        total = sum(nums)

        output, marked = [], set()
        for index, k in queries : 
            if index not in marked :
                marked.add(index)
                total -= nums[index] 
                
            while k != 0 and heap : 
                num, index = heappop(heap)
                if index not in marked :
                    total -= num 
                    k -= 1
                    marked.add(index)
            output.append(total)

        return output