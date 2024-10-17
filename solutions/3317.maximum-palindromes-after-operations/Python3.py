class Solution:
    def maxPalindromesAfterOperations(self, words: list) -> int:
        temp_str = ''.join(words)
        freq_arr = [0] * 26
        for ch in temp_str:
            freq_arr[ord(ch) - ord('a')] += 1
        
        words.sort(key=len)
        one_count, even_count = 0, 0
        
        for x in freq_arr:
            if x % 2 == 0:
                even_count += x
            else:
                even_count += x - 1
                one_count += 1
        
        ans = 0
        for item in words:
            l = len(item)
            if l % 2 == 0 and even_count >= l:
                even_count -= l
                ans += 1
            elif l % 2 != 0 and even_count >= l - 1:
                even_count -= l - 1
                
                if one_count >= 1:
                    one_count -= 1
                    ans += 1
                elif even_count >= 1:
                    even_count -= 1
                    ans += 1
            
        return ans