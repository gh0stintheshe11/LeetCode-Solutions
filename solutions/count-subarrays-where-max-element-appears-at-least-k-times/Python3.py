class Solution:
    def countSubarrays(self, nums: List[int], k: int, ans = 0) -> int:
        queue, left = deque(), -1
        n, mx = len(nums), max(nums)

        for rght, num in enumerate(nums):
            if num == mx:
                queue.append(rght)
                
                if len(queue) == k:
                    ans -= (n-rght) * (left-(left:= queue.popleft()))

        return ans