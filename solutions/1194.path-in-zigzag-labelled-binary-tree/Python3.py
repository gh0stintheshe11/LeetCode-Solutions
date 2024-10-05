class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def get_level(label: int) -> int:
            level = 0
            while (1 << level) <= label:
                level += 1
            return level - 1

        level = get_level(label)
        path = []
        
        while label > 0:
            path.append(label)
            max_num_in_level = (1 << (level + 1)) - 1
            min_num_in_level = 1 << level
            label = (max_num_in_level + min_num_in_level - label) // 2
            level -= 1
        
        return path[::-1]