class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        morse_map = {chr(i + ord('a')): morse for i, morse in enumerate(morse_code)}
        
        transformations = set()
        
        for word in words:
            transformation = ''.join(morse_map[char] for char in word)
            transformations.add(transformation)
        
        return len(transformations)