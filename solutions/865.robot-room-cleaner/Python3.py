class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(cell, d):
            robot.clean()
            visited.add(cell)
            
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])
                
                if new_cell not in visited and robot.move():
                    dfs(new_cell, new_d)
                    go_back()

                robot.turnRight()
                
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dfs((0, 0), 0)