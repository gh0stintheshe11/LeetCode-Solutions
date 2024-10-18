class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        from collections import Counter

        count1 = Counter(word1)
        count2 = Counter(word2)

        distinct1 = len(count1)
        distinct2 = len(count2)

        for char1 in count1:
            for char2 in count2:
                if char1 == char2:
                    if distinct1 == distinct2:
                        return True
                else:
                    new_distinct1 = distinct1
                    new_distinct2 = distinct2

                    if count1[char1] == 1:
                        new_distinct1 -= 1

                    if count2[char2] == 1:
                        new_distinct2 -= 1

                    if count2[char1] == 0:
                        new_distinct2 += 1

                    if count1[char2] == 0:
                        new_distinct1 += 1

                    if new_distinct1 == new_distinct2:
                        return True

        return False