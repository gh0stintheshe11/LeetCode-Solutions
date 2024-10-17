class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = [set() for _ in range(n)]
        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])

        def make_tree(i, parent):
            ancestors[i].add(parent)
            for j in ancestors[parent]:
                ancestors[i].add(j)
            tree[i].remove(parent)
            for child in tree[i]:
                make_tree(child, i)
                xor[i] ^= xor[child]

        xor = [nums[i] for i in range(n)]
        ancestors = [set() for _ in range(n)]
        for child in tree[0]:
            make_tree(child, 0)
            xor[0] ^= xor[child]

        ans = 2 ** 31 - 1
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if i in ancestors[j]:
                    parts = [xor[0] ^ xor[i], xor[i] ^ xor[j], xor[j]]
                elif j in ancestors[i]:
                    parts = [xor[0] ^ xor[j], xor[i], xor[i] ^ xor[j]]
                else:
                    parts = [xor[0] ^ xor[i] ^ xor[j], xor[i], xor[j]]
                ans = min(ans, max(parts) - min(parts))
        return ans