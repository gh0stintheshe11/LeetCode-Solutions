class Solution:
    
    def sortArray(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(arr):
            total = 0
            notSeen = {i for i in range(n)}
            while notSeen:
                current = notSeen.pop()
                start, count, foundZero = current, 0, True if current == 0 else False
                #while not reached an already visited node
                while arr[current] != start:
                    current = arr[current]
                    notSeen.discard(current)
                    count += 1
                    foundZero = foundZero or current == 0
                total += count if foundZero else 0 if not count else count + 2
            return total

        return min(helper(nums), helper([nums[-1]] + nums[:-1]))