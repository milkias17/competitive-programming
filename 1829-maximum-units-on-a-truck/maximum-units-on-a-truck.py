class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s_box_types = sorted(boxTypes, key=lambda x: (x[1], x[0]), reverse=True)
        total_units = 0

        for num_box, num_units in s_box_types:
            if num_box >= truckSize:
                total_units += truckSize * num_units
                break
            
            truckSize -= num_box
            total_units += num_box * num_units
        
        return total_units