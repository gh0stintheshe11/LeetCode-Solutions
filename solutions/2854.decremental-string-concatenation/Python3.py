class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(index: int, first: str, last: str) -> int:
            if index == len(words):
                return 0
            
            word = words[index]
            w_first, w_last, length = word[0], word[-1], len(word)

            # Option 1: Join current result with the new word (end-to-start)
            cost1 = dp(index + 1, first, w_last) + (length - 1 if last == w_first else length)
            
            # Option 2: Join the new word with current result (start-to-end),
            # which means we are considering the word first and then the current result
            cost2 = dp(index + 1, w_first, last) + (length - 1 if w_last == first else length)

            return min(cost1, cost2)

        # Initial call with the first word, its first and last character
        start_word = words[0]
        return len(start_word) + dp(1, start_word[0], start_word[-1])