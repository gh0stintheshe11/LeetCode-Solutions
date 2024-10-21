class Solution:
    def maxOperations(self, s: str) -> int:
        group_num = 0
        counter = {0:0}
        looking_for_zeros = True
        for i in range(len(s)-1, -1, -1):
            if looking_for_zeros == True:
                if s[i] == '1':
                    counter[group_num] += 1
                    continue
                else:
                    group_num += 1
                    counter[group_num] = 0
                    looking_for_zeros = False
                    continue
            else:
                if s[i] == '0':
                    continue
                else:
                    counter[group_num] += 1
                    looking_for_zeros = True
                    continue
        changes = 0
        for group in counter:
            changes += group * counter[group]
        return changes