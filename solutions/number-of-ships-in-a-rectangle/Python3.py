class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        
        return (self.countShips(sea, Point(midX, midY), bottomLeft) +
                self.countShips(sea, topRight, Point(midX+1, midY+1)) +
                self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY+1)) +
                self.countShips(sea, Point(topRight.x, midY), Point(midX+1, bottomLeft.y)))