class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        val_pos_map = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                val_pos_map[mat[i][j]].append((i, j))

        plens_y, plens_x = defaultdict(int), defaultdict(int)
        for val, positions in sorted(val_pos_map.items()):
            new_plens_y, new_plens_x = defaultdict(int), defaultdict(int)
            for y, x in positions:
                curr_max = max(plens_y[y], plens_x[x]) + 1
                new_plens_y[y] = max(new_plens_y[y], curr_max)
                new_plens_x[x] = max(new_plens_x[x], curr_max)

            plens_y.update(new_plens_y)
            plens_x.update(new_plens_x)
        
        return max(max(plens_y.values()), max(plens_x.values()))