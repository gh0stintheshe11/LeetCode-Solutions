from collections import defaultdict
from typing import List

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert_to_minutes(time: str) -> int:
            hh, mm = map(int, time.split(':'))
            return hh * 60 + mm

        times_by_person = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            times_by_person[name].append(convert_to_minutes(time))

        alert_names = set()

        for name, times in times_by_person.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    alert_names.add(name)
                    break

        return sorted(alert_names)