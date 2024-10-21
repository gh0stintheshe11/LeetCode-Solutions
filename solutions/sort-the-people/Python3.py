class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair each name with its corresponding height
        people = list(zip(heights, names))
        
        # Sort the pairs based on heights in descending order
        people.sort(reverse=True, key=lambda x: x[0])
        
        # Extract the names from the sorted pairs
        sorted_names = [name for height, name in people]
        
        return sorted_names