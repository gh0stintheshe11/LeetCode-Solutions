class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words_dict = {word: i for i, word in enumerate(words)}
        results = []

        for index, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words_dict:
                        results.append([words_dict[back], index])
                
                if j != len(word) and is_palindrome(suffix):
                    front = prefix[::-1]
                    if front != word and front in words_dict:
                        results.append([index, words_dict[front]])

        return results