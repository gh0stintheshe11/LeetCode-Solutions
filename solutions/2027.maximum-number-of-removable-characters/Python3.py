class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(removed_set: set) -> bool:
            p_index = 0
            for i in range(len(s)):
                if i in removed_set:  # Skip removed characters
                    continue
                if s[i] == p[p_index]:
                    p_index += 1
                    if p_index == len(p):  # All of p has been matched
                        return True
            return p_index == len(p)

        low, high = 0, len(removable)
        while low < high:
            mid = (low + high + 1) // 2
            if is_subsequence(set(removable[:mid])):
                low = mid
            else:
                high = mid - 1
        return low