class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def buildDifferenceArray(nums):
            n = len(nums)
            nums2 = [0] * (n - 1)
            for i in range(n - 1):
                if nums[i + 1] > nums[i]:
                    nums2[i] = 1
                elif nums[i + 1] == nums[i]:
                    nums2[i] = 0
                else:
                    nums2[i] = -1
            return nums2
        
        def kmpPatternMatch(text, pattern):
            n, m = len(text), len(pattern)
            lps = [0] * m

            j = 0
            i = 1
            while i < m:
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        lps[i] = 0
                        i += 1

            count = 0
            i = 0
            j = 0
            while i < n:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1

                if j == m:
                    count += 1
                    j = lps[j - 1]
                elif i < n and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return count
        
        nums2 = buildDifferenceArray(nums)
        return kmpPatternMatch(nums2, pattern)