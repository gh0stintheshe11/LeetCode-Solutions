class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        goat_latin_words = []
        
        for i, word in enumerate(words):
            if word[0] in vowels:
                goat_word = word + 'ma' + 'a' * (i + 1)
            else:
                goat_word = word[1:] + word[0] + 'ma' + 'a' * (i + 1)
            goat_latin_words.append(goat_word)
        
        return ' '.join(goat_latin_words)