class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def get_prefixes(num):
            s = str(num)
            return {s[:i] for i in range(1, len(s) + 1)}

        prefixes_set = set()
        for num in arr1:
            prefixes_set.update(get_prefixes(num))

        max_length = 0
        for num in arr2:
            prefixes = get_prefixes(num)
            for prefix in prefixes:
                if prefix in prefixes_set:
                    max_length = max(max_length, len(prefix))

        return max_length