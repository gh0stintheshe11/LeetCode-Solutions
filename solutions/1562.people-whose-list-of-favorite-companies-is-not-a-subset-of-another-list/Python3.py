from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(company_list) for company_list in favoriteCompanies]
        result = []
        
        for i, current_set in enumerate(sets):
            if not any(current_set < other_set for j, other_set in enumerate(sets) if i != j):
                result.append(i)
        
        return result