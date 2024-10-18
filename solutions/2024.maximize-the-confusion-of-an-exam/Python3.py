class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutive(answerKey: str, k: int, charToMaximize: str) -> int:
            max_length = 0
            left = 0
            count_changed = 0

            for right in range(len(answerKey)):
                if answerKey[right] != charToMaximize:
                    count_changed += 1
                
                while count_changed > k:
                    if answerKey[left] != charToMaximize:
                        count_changed -= 1
                    left += 1
                
                max_length = max(max_length, right - left + 1)
            return max_length

        return max(maxConsecutive(answerKey, k, 'T'), maxConsecutive(answerKey, k, 'F'))