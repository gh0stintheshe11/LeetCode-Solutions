class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total_damage = sum(damage)
        max_damage = max(damage)
        min_health = total_damage - min(max_damage, armor) + 1
        return min_health