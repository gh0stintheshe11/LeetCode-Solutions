class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlaceBalls(min_distance: int) -> bool:
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= min_distance:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        position.sort()
        left, right = 1, position[-1] - position[0]
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer