class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(c):
            real, imaginary = c.split('+')
            return int(real), int(imaginary[:-1])
        
        r1, i1 = parse_complex(num1)
        r2, i2 = parse_complex(num2)
        
        real_part = r1 * r2 - i1 * i2
        imaginary_part = r1 * i2 + i1 * r2
        
        return f'{real_part}+{imaginary_part}i'