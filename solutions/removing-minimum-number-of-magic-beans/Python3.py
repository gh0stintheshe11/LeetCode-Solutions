class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total_beans = sum(beans)
        n = len(beans)
        min_removal = float('inf')
        
        for i in range(n):
            current_removal = total_beans - (beans[i] * (n - i))
            min_removal = min(min_removal, current_removal)
        
        return min_removal