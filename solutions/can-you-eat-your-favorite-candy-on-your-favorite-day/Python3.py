class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # Prefix sum to get the total candies up to each type
        prefixSum = [0] * len(candiesCount)
        prefixSum[0] = candiesCount[0]
        for i in range(1, len(candiesCount)):
            prefixSum[i] = prefixSum[i - 1] + candiesCount[i]

        answer = []
        
        for favoriteType, favoriteDay, dailyCap in queries:
            # Total candies required to start eating the favorite type
            minCandiesRequired = favoriteDay + 1
            # Max candies one can eat until the favorite day
            maxCandiesPossible = (favoriteDay + 1) * dailyCap
            
            # Earliest candies needed to reach this type
            minCandyNeededForType = prefixSum[favoriteType - 1] + 1 if favoriteType > 0 else 1
            # Total candies available till favorite type
            totalCandyAvailable = prefixSum[favoriteType]
            
            # Check if the favorite day is achievable
            if minCandiesRequired <= totalCandyAvailable and maxCandiesPossible >= minCandyNeededForType:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer