class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        for i in range(n - 1):
            if ((int(chars[i]) % 2 == int(chars[i + 1]) % 2)) and int(chars[i]) > int(chars[i + 1]):
                temp = chars[i]
                chars[i] = chars[i + 1]
                chars[i + 1] = temp
                break
        return "".join(chars)