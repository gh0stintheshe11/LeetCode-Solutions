class Excel:

    def __init__(self, height: int, width: str):
        self.mat = [[0]*(ord(width)-ord("A")+1) for _ in range(height)]
        self.formula_dict = {}

    def set(self, row: int, column: str, val: int) -> None:
        col = ord(column) - ord('A')
        self.mat[row-1][col] = val
        self.formula_dict.pop((row-1, col), None)

    def get(self, row: int, column: str) -> int:
        col = ord(column) - ord('A')
        return self.dfs(row-1, col)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col = ord(column) - ord('A')
        self.formula_dict[(row-1, col)] = numbers
        return self.get(row, column)

    def dfs(self, row: int, col: int) -> int:
        if (row, col) not in self.formula_dict:
            return self.mat[row][col]

        sum_value = 0
        numbers = self.formula_dict[(row, col)]
        
        for item in numbers:
            if ':' in item:
                start, end = item.split(':')
                start_row, start_col = int(start[1:])-1, ord(start[0])-ord('A')
                end_row, end_col = int(end[1:])-1, ord(end[0])-ord('A')
                for r in range(start_row, end_row + 1):
                    for c in range(start_col, end_col + 1):
                        sum_value += self.dfs(r, c)
            else:
                item_row = int(item[1:])-1
                item_col = ord(item[0]) - ord('A')
                sum_value += self.dfs(item_row, item_col)

        return sum_value