class Solution:
    def findLatestTime(self, s: str) -> str:
        # Handle hours part
        if s[0] == '?':
            if s[1] == '?' or s[1] <= '1':
                s = '1' + s[1:]  # able to make '11'
            else:
                s = '0' + s[1:]  # able to make '09'
        
        if s[1] == '?':
            if s[0] == '1':
                s = s[0] + '1' + s[2:]  # make it '11'
            else:
                s = s[0] + '9' + s[2:]  # make it '09'
                
        # Handle minutes part
        if s[3] == '?':
            s = s[:3] + '5' + s[4:]  # make it '59'
        
        if s[4] == '?':
            s = s[:4] + '9'  # make it '59'
        
        return s