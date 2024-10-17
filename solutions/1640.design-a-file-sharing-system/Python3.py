from typing import List
import heapq

class FileSharing:

    def __init__(self, m: int):
        self.m = m
        self.userChunks = {}
        self.chunkOwners = {i: set() for i in range(1, m+1)}
        self.availableIDs = []
        self.nextID = 1

    def join(self, ownedChunks: List[int]) -> int:
        if self.availableIDs:
            userID = heapq.heappop(self.availableIDs)
        else:
            userID = self.nextID
            self.nextID += 1
        self.userChunks[userID] = set(ownedChunks)
        
        for chunk in ownedChunks:
            self.chunkOwners[chunk].add(userID)
            
        return userID

    def leave(self, userID: int) -> None:
        if userID in self.userChunks:
            for chunk in self.userChunks[userID]:
                self.chunkOwners[chunk].remove(userID)
            del self.userChunks[userID]
            heapq.heappush(self.availableIDs, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        if chunkID in self.chunkOwners:
            owners = sorted(self.chunkOwners[chunkID])
            if owners:
                self.userChunks[userID].add(chunkID)
                self.chunkOwners[chunkID].add(userID)
            return owners
        return []