class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        distribution = [0] * num_people
        i = 0
        while candies > 0:
            distribution[i % num_people] += min(candies, i + 1)
            candies -= min(candies, i + 1)
            i += 1
        return distribution