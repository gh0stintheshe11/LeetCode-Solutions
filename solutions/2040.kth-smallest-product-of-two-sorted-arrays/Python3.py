class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        def fn(val):
            """Return count of products <= val."""
            ans = 0
            for x in nums1: 
                if x < 0: ans += len(nums2) - bisect_left(nums2, ceil(val/x))
                elif x == 0: 
                    if 0 <= val: ans += len(nums2)
                else: ans += bisect_right(nums2, floor(val/x))
            return ans 
            
        lo, hi = -10**10, 10**10 + 1
        while lo < hi: 
            mid = lo + hi >> 1
            if fn(mid) < k: lo = mid + 1
            else: hi = mid
        return lo