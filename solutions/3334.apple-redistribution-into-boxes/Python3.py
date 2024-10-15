class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        boxes_used = 0
        current_capacity = 0
        
        for c in capacity:
            current_capacity += c
            boxes_used += 1
            if current_capacity >= total_apples:
                return boxes_used
        
        return boxes_used