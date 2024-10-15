from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        
        # Convert each person's skills to a bitmask
        people_skills = []
        for person in people:
            mask = 0
            for skill in person:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            people_skills.append(mask)
        
        # DP dictionary to store the smallest team for each skill set
        dp = {0: []}
        
        for i, person_skill in enumerate(people_skills):
            if person_skill == 0:
                continue
            new_dp = dp.copy()
            for skill_set, team in dp.items():
                new_skill_set = skill_set | person_skill
                if new_skill_set == skill_set:
                    continue
                if new_skill_set not in new_dp or len(new_dp[new_skill_set]) > len(team) + 1:
                    new_dp[new_skill_set] = team + [i]
            dp = new_dp
        
        return dp[(1 << n) - 1]