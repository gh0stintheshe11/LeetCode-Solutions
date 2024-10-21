class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for char in s:
            if char == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count