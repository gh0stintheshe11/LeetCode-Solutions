class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.ptr = 0
        self.current_char = ''
        self.current_count = 0

    def next(self) -> str:
        if self.current_count == 0:
            if self.ptr >= len(self.compressedString):
                return ' '
            
            self.current_char = self.compressedString[self.ptr]
            self.ptr += 1
            
            count_str = []
            while self.ptr < len(self.compressedString) and self.compressedString[self.ptr].isdigit():
                count_str.append(self.compressedString[self.ptr])
                self.ptr += 1
            self.current_count = int(''.join(count_str))
        
        self.current_count -= 1
        return self.current_char

    def hasNext(self) -> bool:
        return self.current_count > 0 or self.ptr < len(self.compressedString)