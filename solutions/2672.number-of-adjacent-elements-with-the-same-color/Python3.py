class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        current_count = 0
        result = []
        
        for index, color in queries:
            if colors[index] != 0:
                if index > 0 and colors[index] == colors[index - 1]:
                    current_count -= 1
                if index < n - 1 and colors[index] == colors[index + 1]:
                    current_count -= 1

            colors[index] = color
            
            if index > 0 and colors[index] == colors[index - 1]:
                current_count += 1
            if index < n - 1 and colors[index] == colors[index + 1]:
                current_count += 1
                
            result.append(current_count)
        
        return result