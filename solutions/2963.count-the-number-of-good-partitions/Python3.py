class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:

        first = {}
        last = {}

        for idx, num in enumerate(nums):
            if num not in first:
                first[num] = idx
            last[num] = idx
        
        itvs = sorted(((first[num], last[num]) for num in set(nums)))
        
        group_count = 1
        curr = itvs[0]

        for i in range(1, len(itvs)):
            l, r = itvs[i]
            cl, cr = curr
            if cr > l and cl < r:
                cr = max(cr, r)
                curr = (cl, cr)
            else:
                group_count += 1
                curr = (l, r)

        return pow(2, group_count - 1, 10 ** 9 + 7)