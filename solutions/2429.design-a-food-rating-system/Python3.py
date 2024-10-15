from sortedcontainers import SortedSet
from collections import defaultdict
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_details = {food: (cuisine, rating) for food, cuisine, rating in zip(foods, cuisines, ratings)}
        self.cuisine_to_foods = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisine_to_foods[cuisine].add((rating, food))
    
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.food_to_details[food]
        self.cuisine_to_foods[cuisine].remove((oldRating, food))
        self.cuisine_to_foods[cuisine].add((newRating, food))
        self.food_to_details[food] = (cuisine, newRating)
    
    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_to_foods[cuisine][0][1]