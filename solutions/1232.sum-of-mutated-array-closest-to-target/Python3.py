class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calculate_sum_with_value(x):
            return sum(min(num, x) for num in arr)
        
        left, right = 0, max(arr)
        best_value = right
        closest_diff = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            current_sum = calculate_sum_with_value(mid)
            current_diff = abs(current_sum - target)
            
            if current_diff < closest_diff:
                closest_diff = current_diff
                best_value = mid
            elif current_diff == closest_diff and mid < best_value:
                best_value = mid
            
            if current_sum < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return best_value