class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        # Try buying 0 to maximum possible pens with the given total
        for pens in range(total // cost1 + 1):
            remaining_money = total - pens * cost1
            # Calculate how many pencils we can buy with the remaining money
            ways += remaining_money // cost2 + 1
        return ways