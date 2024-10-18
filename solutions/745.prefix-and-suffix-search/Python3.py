class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_suffix_map = {}
        for i, word in enumerate(words):
            prefix_suffix_combinations = [word[:k] + '{' + word[j:] for k in range(len(word) + 1) for j in range(len(word) + 1)]
            for combination in prefix_suffix_combinations:
                self.prefix_suffix_map[combination] = i

    def f(self, pref: str, suff: str) -> int:
        search_key = pref + '{' + suff
        return self.prefix_suffix_map.get(search_key, -1)