class Solution:
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        total_chars = 0
        buf4 = [''] * 4
        
        while total_chars < n:
            chars_read = read4(buf4)
            if chars_read == 0:
                break
            
            chars_to_write = min(chars_read, n - total_chars)
            buf[total_chars:total_chars + chars_to_write] = buf4[:chars_to_write]
            total_chars += chars_to_write
            
        return total_chars