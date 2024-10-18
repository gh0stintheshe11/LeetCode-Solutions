class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        loginMinutes = timeToMinutes(loginTime)
        logoutMinutes = timeToMinutes(logoutTime)
        
        if logoutMinutes < loginMinutes:
            logoutMinutes += 24 * 60
        
        startRound = (loginMinutes + 14) // 15  # Round up to the nearest quarter
        endRound = logoutMinutes // 15  # Round down to the nearest quarter
        
        return max(0, endRound - startRound)