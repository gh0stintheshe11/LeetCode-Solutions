from sortedcontainers import SortedList
from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = [-1] * (n-k+1)

        count = Counter()
        for i in range(k-1):
            count[nums[i]] += 1

        topX = SortedList()
        other = SortedList([(count[num], num) for num in set(nums)])
        while other and len(topX) < x:
            topX.add(other.pop())

        sumX = sum(num*freq for freq, num in topX)

        for i in range(k-1, n):
            # add new item to sliding window
            old_item = (count[nums[i]], nums[i])
            if old_item in topX:
                topX.remove(old_item)
                sumX -= old_item[0]*old_item[1] # only item in topX effect sumX
            else:
                other.remove(old_item)

            count[nums[i]] += 1
            item = (count[nums[i]], nums[i])
            topX.add(item)
            sumX += item[0]*item[1]
            while topX and len(topX) > x:
                sumX -= topX[0][0] * topX[0][1] # only item in topX effect sumX
                other.add(topX.pop(0))

            # calculate X sum
            answer[i-k+1] = sumX

            # remove old item from sliding window
            old_item = (count[nums[i-k+1]], nums[i-k+1])
            if old_item in topX:
                topX.remove(old_item)
                sumX -= old_item[0]*old_item[1] # only item in topX effect sumX
            else:
                other.remove(old_item)

            count[nums[i-k+1]] -= 1
            other.add((count[nums[i-k+1]], nums[i-k+1]))
            while other and len(topX) < x:
                sumX += other[-1][0] * other[-1][1] # only item in topX effect sumX
                topX.add(other.pop())
        return answer