class Solution:
    def maximumLength(self, s: str) -> int:
        def plus(i, j, dic, s):
            for k in range(3):
                if i + k >= j:
                    continue
                if s[i+k:j] not in dic:
                    dic[s[i+k:j]] = k + 1
                else:
                    dic[s[i+k:j]] += k + 1

        def findLongest(longest, dic):
            for i in dic:
                if dic[i] >= 3 and len(i) > longest:
                    longest = len(i)
            return longest

        i = 0
        j = 0
        n = len(s)
        dic = {}
        while j < n:
            if s[j] == s[i]:
                j += 1
            else:
                plus(i, j, dic, s)
                i = j
        plus(i, j, dic, s)
        return findLongest(-1, dic)