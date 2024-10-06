class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(index, current):
            if not is_unique(current):
                return 0
            if index == len(arr):
                return len(current)
            
            without_current = backtrack(index + 1, current)
            with_current = backtrack(index + 1, current + arr[index])
            
            return max(without_current, with_current)
        
        return backtrack(0, "")