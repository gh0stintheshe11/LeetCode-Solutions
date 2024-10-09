class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedList

        nums.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))

        answer = [-1] * len(queries)
        sorted_list = SortedList()
        trie_root = {}

        for m, x, i in queries:
            while nums and nums[0] <= m:
                num = nums.pop(0)
                sorted_list.add(num)
                node = trie_root
                for k in range(31, -1, -1):
                    bit = (num >> k) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]

            if sorted_list:
                node = trie_root
                max_xor = 0
                for k in range(31, -1, -1):
                    bit = (x >> k) & 1
                    toggled_bit = 1 - bit
                    if toggled_bit in node:
                        max_xor |= (1 << k)
                        node = node[toggled_bit]
                    else:
                        node = node[bit]
                answer[i] = max_xor

        return answer