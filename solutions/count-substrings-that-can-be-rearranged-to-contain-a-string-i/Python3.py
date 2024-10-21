class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        l, r = 0, 0
        f_2, f_1 = [0]*26, [0]*26
        m = n2
        ans = 0
        for c in word2:
            f_2[ord(c)-ord('a')] += 1

        while r < n1:
            i = ord(word1[r])-ord('a')
            f_1[i] += 1
            if f_2[i] != 0 and f_2[i] >= f_1[i] :
                m -= 1
            while m == 0:
                ans += n1-r
                #exclude left and move left
                i_e = ord(word1[l])-ord('a')
                f_1[i_e] -= 1
                if f_2[i_e] != 0 and f_2[i_e] > f_1[i_e] :
                    m += 1
                l += 1
            r += 1
        return ans