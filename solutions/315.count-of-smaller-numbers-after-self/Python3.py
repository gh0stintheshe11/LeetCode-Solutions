class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(enums):
            mid = len(enums) // 2
            if mid:
                left, right = merge_sort(enums[:mid]), merge_sort(enums[mid:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        smaller[left[i][0]] += j
                        enums[i+j] = left[i]
                        i += 1
                    else:
                        enums[i+j] = right[j]
                        j += 1
            return enums
        
        smaller = [0] * len(nums)
        merge_sort(list(enumerate(nums)))
        return smaller