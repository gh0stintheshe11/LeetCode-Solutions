class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        length = len(chars)
        write_index = 0
        
        while i < length:
            char = chars[i]
            count = 0

            while i < length and chars[i] == char:
                count += 1
                i += 1
            
            chars[write_index] = char
            write_index += 1

            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1
        
        return write_index