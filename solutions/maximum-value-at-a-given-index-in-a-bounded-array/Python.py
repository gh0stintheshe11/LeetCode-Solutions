class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def calculate_sum(value, length):
            if value >= length:
                return (value + value - length + 1) * length // 2
            else:
                return (value + 1) * value // 2 + (length - value)
        
        def is_valid(value):
            left_length = index
            right_length = n - index - 1
            left_sum = calculate_sum(value - 1, left_length)
            right_sum = calculate_sum(value - 1, right_length)
            total_sum = left_sum + right_sum + value
            return total_sum <= maxSum
        
        low, high = 1, maxSum
        while low < high:
            mid = (low + high + 1) // 2
            if is_valid(mid):
                low = mid
            else:
                high = mid - 1
        
        return low