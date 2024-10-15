class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        chars = list(s)
        n = len(chars)
        moves = 0

        left, right = 0, n - 1
        while left < right:
            if chars[left] == chars[right]:
                left += 1
                right -= 1
            else:
                k = right
                while chars[k] != chars[left]:
                    k -= 1

                if k == left:
                    chars[left], chars[left + 1] = chars[left + 1], chars[left]
                    moves += 1
                else:
                    while k < right:
                        chars[k], chars[k + 1] = chars[k + 1], chars[k]
                        moves += 1
                        k += 1
                    left += 1
                    right -= 1
        
        return moves