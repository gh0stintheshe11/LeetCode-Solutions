class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        right = []
        left = []
        rightReady = []
        leftReady = [(-t[0] - t[2], -i) for i, t in enumerate(time)]
        heapify(leftReady)
        currTime = 0

        def getWorkersReady(t):
            def transfer(heap, readyHeap):
                while heap and heap[0][0] <= t:
                    _, speed, neg_i = heappop(heap)
                    heappush(readyHeap, (speed, neg_i))
            transfer(left, leftReady)
            transfer(right, rightReady)

        while n:
            getWorkersReady(currTime)
            if rightReady:
                speed, neg_i = heappop(rightReady)
                currTime += time[abs(neg_i)][2]
                n -= 1
                heappush(left, (currTime + time[abs(neg_i)][3], speed, neg_i))
            elif len(right) == n:
                currTime = right[0][0]
            elif leftReady:
                speed, neg_i = heappop(leftReady)
                currTime += time[abs(neg_i)][0]
                heappush(right, (currTime + time[abs(neg_i)][1], speed, neg_i))
            else:
                currTime = min(
                    right[0][0] if right else float("inf"),
                    left[0][0] if left else float("inf")
                )
        return currTime