class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0
        for s in strs:
            if s.isdigit():
                current_value = int(s)
            else:
                current_value = len(s)
            max_value = max(max_value, current_value)
        return max_value