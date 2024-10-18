from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initial set of available supplies
        supply_set = set(supplies)
        
        # Create a map to track remaining dependencies (ingredients) for each recipe
        indegrees = {recipe: len(ingredients[i]) for i, recipe in enumerate(recipes)}
        
        # Create a dependency graph where each recipe points to recipes requiring it
        graph = defaultdict(list)
        for i, ingr_list in enumerate(ingredients):
            for ingr in ingr_list:
                graph[ingr].append(recipes[i])
        
        # Add all directly available recipes (with no ingredients to be satisfied) to the queue
        queue = deque()
        for i, recipe in enumerate(recipes):
            if indegrees[recipe] == 0:
                queue.append(recipe)

        # Add all initial supplies as potential throughputs
        queue.extend(supply_set)
        
        possible_recipes = set()

        # Start processing the queue
        while queue:
            current = queue.popleft()
            
            # If the current item is a recipe, add it to possible recipes
            if current in indegrees:
                possible_recipes.add(current)
            
            # For all recipes that depend on the current item
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:  # All dependencies for this recipe are satisfied
                    queue.append(neighbor)

        return list(possible_recipes)