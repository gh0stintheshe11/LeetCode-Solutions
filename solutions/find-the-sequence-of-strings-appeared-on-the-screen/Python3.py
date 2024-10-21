class Solution:
    def stringSequence(self, target: str) -> List[str]:
        prefix = []
        result = []

        for c in target:
            prefix.append("")
            
            for i in range(ord("a"), ord(c) + 1):
                prefix[-1] = chr(i)
                result.append(''.join(prefix))

        return result