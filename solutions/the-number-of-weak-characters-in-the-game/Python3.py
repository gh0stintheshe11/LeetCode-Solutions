class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Step 1: Sort properties by attack in descending order, and by defense in ascending order if attack is the same
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        max_defense = 0
        weak_characters = 0
        
        # Step 2: Traverse through the sorted properties list
        for _, defense in properties:
            # If the current defense is less than the max_defense encountered so far, it is a weak character
            if defense < max_defense:
                weak_characters += 1
            else:
                # Update the max_defense encountered so far
                max_defense = defense
                
        return weak_characters