class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:

        dp={}

        def dfs(index,char_bitmask=0,change_used=0):
            nonlocal k
            if index>=len(s):
                return 1
            
            if (index,char_bitmask,change_used) in dp:
                return dp[(index,char_bitmask,change_used)]

            val=0
            bitmask_cur_char = 1<<(ord(s[index])-ord("a"))

            if (char_bitmask|bitmask_cur_char).bit_count()>k:
                val=max(val,1+dfs(index+1,bitmask_cur_char,change_used))
            else:
                val=max(val,dfs(index+1,char_bitmask|bitmask_cur_char,change_used))

            if change_used==0:

                for i in range(26):
                    bitmask_brute_char = 1<<i
                    if bitmask_brute_char & char_bitmask:
                        continue
                    if (char_bitmask|bitmask_brute_char).bit_count()>k:
                        val=max(val,1+dfs(index+1,bitmask_brute_char,1))
                    else:
                        val=max(val,dfs(index+1,char_bitmask|bitmask_brute_char,1))

            dp[(index,char_bitmask,change_used)]=val

            return dp[(index,char_bitmask,change_used)]

        return dfs(0)