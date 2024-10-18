class Solution:
    def maximumTime(self, time: str) -> str:
        hours, minutes = time.split(':')
        
        if hours[0] == '?':
            if hours[1] == '?' or hours[1] <= '3':
                hours = '2' + hours[1]
            else:
                hours = '1' + hours[1]
        
        if hours[1] == '?':
            if hours[0] == '2':
                hours = hours[0] + '3'
            else:
                hours = hours[0] + '9'
        
        if minutes[0] == '?':
            minutes = '5' + minutes[1]
        
        if minutes[1] == '?':
            minutes = minutes[0] + '9'
        
        return f"{hours}:{minutes}"