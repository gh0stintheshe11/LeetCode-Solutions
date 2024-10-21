class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # Number of elements in the sample
        total_count = sum(count)
        
        # Minimum and maximum values
        min_val = next(i for i, x in enumerate(count) if x > 0)
        max_val = next(i for i, x in enumerate(reversed(count)) if x > 0)
        max_val = 255 - max_val
        
        # Calculate mean
        sum_total = sum(i * count[i] for i in range(256))
        mean_val = sum_total / total_count
        
        # Calculate mode
        mode_val = count.index(max(count))
        
        # Calculate median
        mid_count = total_count // 2
        if total_count % 2 == 1:
            median_val = self.findKth(count, mid_count + 1)
        else:
            median_val = (self.findKth(count, mid_count) + self.findKth(count, mid_count + 1)) / 2
        
        return [float(min_val), float(max_val), float(mean_val), float(median_val), float(mode_val)]
    
    def findKth(self, count, k):
        prefix_sum = 0
        for i in range(256):
            prefix_sum += count[i]
            if prefix_sum >= k:
                return i