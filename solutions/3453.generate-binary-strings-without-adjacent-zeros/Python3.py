class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(current, last_char):
            if len(current) == n:
                result.append(current)
                return
            if last_char == '0':
                backtrack(current + '1', '1')
            else:
                backtrack(current + '0', '0')
                backtrack(current + '1', '1')

        result = []
        backtrack('', None)
        return result