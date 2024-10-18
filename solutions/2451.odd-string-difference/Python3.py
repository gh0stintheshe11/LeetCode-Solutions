class Solution:
    def oddString(self, words: List[str]) -> str:
        def difference_array(word):
            return [ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)]

        differences = [difference_array(word) for word in words]
        
        # Count frequency of each difference array
        from collections import Counter
        diff_count = Counter(tuple(diff) for diff in differences)
        
        for word, diff in zip(words, differences):
            if diff_count[tuple(diff)] == 1:
                return word