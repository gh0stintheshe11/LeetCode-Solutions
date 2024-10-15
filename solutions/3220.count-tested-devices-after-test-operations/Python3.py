class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_count = 0
        
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > tested_count:
                tested_count += 1
                
        return tested_count