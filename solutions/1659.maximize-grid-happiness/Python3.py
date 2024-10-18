class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        from functools import lru_cache

        introvert_value, extrovert_value = 120, 40
        introvert_neighbor_penalty, extrovert_neighbor_bonus = -30, 20
        
        @lru_cache(None)
        def dfs(pos, introverts, extroverts, prev_row):
            if pos == m * n or (introverts == 0 and extroverts == 0):
                return 0
            
            current_row, current_col = divmod(pos, n)
            next_cell = pos + 1

            best = dfs(next_cell, introverts, extroverts, prev_row * 3 % (3**n))
            
            for person in [(introvert_value, -1, introvert_neighbor_penalty), 
                           (extrovert_value, 1, extrovert_neighbor_bonus)]:
                person_value, introvert_change, neighbor_impact = person
                
                if introvert_change == -1 and introverts > 0:
                    i_effect = person_value
                    neighbors_effect = 0
                    
                    if current_row > 0:
                        above_person_type = (prev_row // (3**(n-1))) % 3
                        neighbors_effect += (introvert_neighbor_penalty if above_person_type == 1 else 0)
                        neighbors_effect += (extrovert_neighbor_bonus if above_person_type == 2 else 0)
                        i_effect += (neighbor_impact if above_person_type != 0 else 0)
                    
                    if current_col > 0:
                        left_person_type = prev_row % 3
                        neighbors_effect += (introvert_neighbor_penalty if left_person_type == 1 else 0)
                        neighbors_effect += (extrovert_neighbor_bonus if left_person_type == 2 else 0)
                        i_effect += (neighbor_impact if left_person_type != 0 else 0)
                    
                    new_happiness = dfs(next_cell, introverts - 1, extroverts, (prev_row % (3**(n-1))) * 3 + 1)
                    best = max(best, i_effect + neighbors_effect + new_happiness)

                if introvert_change == 1 and extroverts > 0:
                    e_effect = person_value
                    neighbors_effect = 0
                    
                    if current_row > 0:
                        above_person_type = (prev_row // (3**(n-1))) % 3
                        neighbors_effect += (introvert_neighbor_penalty if above_person_type == 1 else 0)
                        neighbors_effect += (extrovert_neighbor_bonus if above_person_type == 2 else 0)
                        e_effect += (neighbor_impact if above_person_type != 0 else 0)
                    
                    if current_col > 0:
                        left_person_type = prev_row % 3
                        neighbors_effect += (introvert_neighbor_penalty if left_person_type == 1 else 0)
                        neighbors_effect += (extrovert_neighbor_bonus if left_person_type == 2 else 0)
                        e_effect += (neighbor_impact if left_person_type != 0 else 0)
                    
                    new_happiness = dfs(next_cell, introverts, extroverts - 1, (prev_row % (3**(n-1))) * 3 + 2)
                    best = max(best, e_effect + neighbors_effect + new_happiness)
            
            return best
        
        return dfs(0, introvertsCount, extrovertsCount, 0)