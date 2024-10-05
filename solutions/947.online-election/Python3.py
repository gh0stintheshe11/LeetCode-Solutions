from collections import defaultdict
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leads = []
        self.times = times
        count = defaultdict(int)
        lead = -1
        
        for i, person in enumerate(persons):
            count[person] += 1
            if count[person] >= count[lead]:
                lead = person
            self.leads.append(lead)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leads[idx]