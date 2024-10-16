
class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        weights = [Counter(word[i] for word in wordlist) for i in range(6)]

        wordlist.sort(key=lambda word: sum(weights[i][c] for i, c in enumerate(word)))

        while wordlist:
            word = wordlist.pop()
            matches = master.guess(word)
            wordlist = [
                other
                for other in wordlist
                if matches == sum(w == o for w, o in zip(word, other))
            ]
