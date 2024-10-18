class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        occupied_positions = set(nums)

        for frm, to in zip(moveFrom, moveTo):
            if frm in occupied_positions:
                occupied_positions.remove(frm)
            occupied_positions.add(to)

        return sorted(occupied_positions)