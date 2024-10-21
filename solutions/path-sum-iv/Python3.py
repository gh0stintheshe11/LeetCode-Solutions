class Solution:
    def pathSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        tree = defaultdict(int)
        for num in nums:
            depth, pos, value = num // 100, (num // 10) % 10, num % 10
            tree[(depth, pos)] = value

        def dfs(node, curr_sum):
            depth, pos = node
            if (depth, pos) not in tree:
                return 0
            curr_sum += tree[(depth, pos)]
            left_child = (depth + 1, 2 * pos - 1)
            right_child = (depth + 1, 2 * pos)
            if left_child not in tree and right_child not in tree:
                return curr_sum
            return dfs(left_child, curr_sum) + dfs(right_child, curr_sum)

        return dfs((1, 1), 0)