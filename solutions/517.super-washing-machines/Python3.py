class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        target = total // n
        max_moves = 0
        curr_balance = 0

        for dresses in machines:
            diff = dresses - target
            curr_balance += diff
            max_moves = max(max_moves, abs(curr_balance), diff)
        
        return max_moves