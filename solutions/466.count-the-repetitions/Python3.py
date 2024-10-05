class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        indexr, countr = {}, {}
        s1_count = s2_count = index = 0
        
        while s1_count < n1:
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2_count += 1
                        index = 0
            s1_count += 1

            if index in indexr:
                s1_start, s2_start = indexr[index], countr[index]
                pre_s1_count = s1_start
                pre_s2_count = s2_start
                
                pattern_s1_count = s1_count - s1_start
                pattern_s2_count = s2_count - s2_start

                repeat = (n1 - pre_s1_count) // pattern_s1_count
                remained_s1_count = (n1 - pre_s1_count) % pattern_s1_count
                
                total_s2_count = pre_s2_count + repeat * pattern_s2_count

                for _ in range(remained_s1_count):
                    for char in s1:
                        if char == s2[index]:
                            index += 1
                            if index == len(s2):
                                total_s2_count += 1
                                index = 0
                return total_s2_count // n2

            indexr[index] = s1_count
            countr[index] = s2_count
        
        return s2_count // n2