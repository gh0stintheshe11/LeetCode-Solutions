class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_search(mountain_arr, target, left, right, ascending=True):
            while left <= right:
                mid = (left + right) // 2
                mid_val = mountain_arr.get(mid)
                
                if mid_val == target:
                    return mid
                if ascending:
                    if mid_val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if mid_val < target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        length = mountain_arr.length()
        
        # Find peak
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left

        # Try to find target on the ascending part
        index = binary_search(mountain_arr, target, 0, peak, ascending=True)
        if index != -1:
            return index
        
        # Try to find target on the descending part
        return binary_search(mountain_arr, target, peak + 1, length - 1, ascending=False)