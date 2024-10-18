class DetectSquares:

    def __init__(self):
        # Store frequency of each point
        self.points_count = {}
    
    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) in self.points_count:
            self.points_count[(x, y)] += 1
        else:
            self.points_count[(x, y)] = 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total_squares = 0
        
        # Check all points with the same y-coordinate
        for (px, py) in self.points_count:
            if py == y and px != x:
                # Calculate potential side length of the square
                side_length = abs(px - x)
                
                # Calculate possible square coordinates
                # Check if the points that can form a square are in the points_count
                if (x, y + side_length) in self.points_count and (px, y + side_length) in self.points_count:
                    total_squares += self.points_count[(px, y)] * self.points_count[(x, y + side_length)] * self.points_count[(px, y + side_length)]
                
                if (x, y - side_length) in self.points_count and (px, y - side_length) in self.points_count:
                    total_squares += self.points_count[(px, y)] * self.points_count[(x, y - side_length)] * self.points_count[(px, y - side_length)]
        
        return total_squares