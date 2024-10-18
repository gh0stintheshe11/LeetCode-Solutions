class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_row_devices = 0
        total_beams = 0
        
        for row in bank:
            current_row_devices = row.count('1')
            if current_row_devices > 0:
                total_beams += prev_row_devices * current_row_devices
                prev_row_devices = current_row_devices
        
        return total_beams