class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k % n
        encrypted_string = ''
        for i in range(n):
            encrypted_string += s[(i + k) % n]
        return encrypted_string