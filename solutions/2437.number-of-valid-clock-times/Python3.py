class Solution:
    def countTime(self, time: str) -> int:
        hh, mm = time.split(':')

        # Calculate possible hours
        if hh == "??":
            possible_hours = 24
        elif hh[0] == '?':
            if hh[1] >= '4':  # ensure hh[1] <= '9'
                possible_hours = 2  # only '0' or '1'
            else:
                possible_hours = 3  # times can start with '0', '1', or '2'
        elif hh[1] == '?':
            if hh[0] == '2':  # 20-23
                possible_hours = 4
            else:  # 00-19
                possible_hours = 10
        else:
            possible_hours = 1
        
        # Calculate possible minutes
        if mm == "??":
            possible_minutes = 60
        elif mm[0] == '?':
            possible_minutes = 6  # 00, 10, 20, ..., 50
        elif mm[1] == '?':
            possible_minutes = 10  # 00-09
        else:
            possible_minutes = 1

        return possible_hours * possible_minutes