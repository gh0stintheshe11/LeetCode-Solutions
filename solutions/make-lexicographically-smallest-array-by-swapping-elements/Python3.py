class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        from collections import deque
        
        sorted_nums = sorted(nums)
        initial_num = sorted_nums[0]
        initial_group = deque([initial_num])
        sorted_groups = [initial_group]
        num_to_group = {initial_num: initial_group}

        for num in sorted_nums[1:]:
            prev_group = sorted_groups[-1]
            if num - prev_group[-1] <= limit:
                prev_group.append(num)
            else:
                prev_group = deque([num])
                sorted_groups.append(prev_group)
            num_to_group[num] = prev_group

        res = []
        for num in nums:
            group = num_to_group[num]
            res.append(group.popleft())
        return res