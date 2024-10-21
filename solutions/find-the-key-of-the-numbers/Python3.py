class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Convert each number to a four-character string with leading zeros
        str1 = f"{num1:04}"
        str2 = f"{num2:04}"
        str3 = f"{num3:04}"
        
        # Generate the key by taking the minimum digit from each position
        key = ''.join(min(str1[i], str2[i], str3[i]) for i in range(4))
        
        # Convert the resultant key to an integer (to remove leading zeros)
        return int(key)