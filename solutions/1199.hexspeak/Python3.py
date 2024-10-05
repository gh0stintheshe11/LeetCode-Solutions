class Solution:
    def toHexspeak(self, num: str) -> str:
        hex_string = hex(int(num))[2:].upper()
        hex_string = hex_string.replace('0', 'O').replace('1', 'I')
        for char in hex_string:
            if char not in {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}:
                return "ERROR"
        return hex_string