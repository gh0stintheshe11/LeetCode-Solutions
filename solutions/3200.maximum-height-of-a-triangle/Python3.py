class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def max_possible_height(red, blue):
            height = 0
            while True:
                height += 1
                if height % 2 == 1:  # Odd rows
                    if red >= height:
                        red -= height
                    else:
                        break
                else:  # Even rows
                    if blue >= height:
                        blue -= height
                    else:
                        break
            return height - 1
        
        # Check the height starting with the first row being red
        max_height_red_start = max_possible_height(red, blue)
        # Check the height starting with the first row being blue
        max_height_blue_start = max_possible_height(blue, red)
        
        return max(max_height_red_start, max_height_blue_start)