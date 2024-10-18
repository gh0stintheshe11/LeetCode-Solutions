class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = float('inf')
        current_whites = 0

        # Calculate whites in the first k-block window
        for i in range(k):
            if blocks[i] == 'W':
                current_whites += 1
        min_recolors = current_whites

        # Slide the window across the rest of the blocks
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_whites -= 1
            if blocks[i] == 'W':
                current_whites += 1
            min_recolors = min(min_recolors, current_whites)

        return min_recolors