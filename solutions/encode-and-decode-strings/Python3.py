class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f'{len(s):04}:{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        decoded = []
        while i < len(s):
            length = int(s[i:i+4])
            i += 5
            decoded.append(s[i:i+length])
            i += length
        return decoded

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))