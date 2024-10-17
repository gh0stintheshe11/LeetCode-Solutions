class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        n = len(nums)
        
        trie = {}
        def add_trie(x):
            node = trie
            for c in bin(x)[2:].zfill(20):
                node = node.setdefault(c, {})
                node['*'] = node.get('*', 0) + 1
        
        def red_trie(x):
            node = trie
            for c in bin(x)[2:].zfill(20):
                node = node[c]
                node['*'] -= 1
                
        j = 0
        for i, num in enumerate(nums):
            add_trie(num)
            while j < i and nums[j] * 2 < num: 
                red_trie(nums[j])
                j += 1
            
            node = trie
            tmp = ""
            for c in bin(num)[2:].zfill(20):
                rev = str(1-int(c))
                if rev in node and node[rev]['*']:
                    node = node[rev]
                    tmp += rev
                else:
                    node = node[c]
                    tmp += c
            ans = max(ans, num ^ int(tmp, 2))
        
        return ans