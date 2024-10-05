class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        subs = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                subs.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        
        return ''.join(sorted(subs, reverse=True))

# Example usage:
# sol = Solution()
# print(sol.makeLargestSpecial("11011000"))  # Output should be "11100100"