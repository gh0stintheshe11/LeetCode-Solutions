from typing import List

class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        
        for i in range(n - 1):
            if sensor1[i] != sensor2[i]:
                # Check if the remainder of the sensors can be made equal by dropping one item
                s1_defective = all(sensor1[k] == sensor2[k + 1] for k in range(i, n - 1))
                s2_defective = all(sensor2[k] == sensor1[k + 1] for k in range(i, n - 1))

                if s1_defective and not s2_defective:
                    return 1
                if s2_defective and not s1_defective:
                    return 2
                
                return -1
        
        return -1