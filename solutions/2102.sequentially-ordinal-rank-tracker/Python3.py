from sortedcontainers import SortedList

class SORTracker:
    def __init__(self):
        self.storage = SortedList()
        self.queryNum = 0
    
    def add(self, name: str, score: int) -> None:
        self.storage.add((-score, name))    

    def get(self) -> str:
        ans = self.storage[self.queryNum]
        self.queryNum += 1
        return ans[1]