class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the boxTypes by number of units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        for number_of_boxes, units_per_box in boxTypes:
            if truckSize <= 0:
                break
            # Take as many boxes as possible, but not more than truckSize
            boxes_to_take = min(truckSize, number_of_boxes)
            total_units += boxes_to_take * units_per_box
            truckSize -= boxes_to_take
        
        return total_units