class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Step 1: Count the frequency of each string
        frequency = {}
        for string in arr:
            if string in frequency:
                frequency[string] += 1
            else:
                frequency[string] = 1
        
        # Step 2: Collect distinct strings
        distinct_strings = []
        for string in arr:
            if frequency[string] == 1:
                distinct_strings.append(string)
        
        # Step 3: Return the kth distinct string if it exists
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""