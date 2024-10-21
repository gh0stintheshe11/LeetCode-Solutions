class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num_str, target):
            def dfs(index, current_sum):
                if index == len(num_str):
                    return current_sum == target
                
                for i in range(index + 1, len(num_str) + 1):
                    part = int(num_str[index:i])
                    if dfs(i, current_sum + part):
                        return True

                return False

            return dfs(0, 0)

        punishment_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                punishment_sum += i * i
        
        return punishment_sum