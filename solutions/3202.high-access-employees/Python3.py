from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def time_difference(t1: str, t2: str) -> int:
            h1, m1 = int(t1[:2]), int(t1[2:])
            h2, m2 = int(t2[:2]), int(t2[2:])
            return (h2 - h1) * 60 + (m2 - m1)
        
        employee_times = defaultdict(list)
        
        for name, time in access_times:
            employee_times[name].append(time)
        
        high_access_employees = set()
        
        for name, times in employee_times.items():
            times.sort()
            for i in range(len(times) - 2):
                if time_difference(times[i], times[i + 2]) < 60:
                    high_access_employees.add(name)
                    break
        
        return list(high_access_employees)