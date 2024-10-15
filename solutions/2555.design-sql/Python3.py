from typing import List, Dict

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: {"columns": columns[i], "rows": {}, "next_id": 1} for i, name in enumerate(names)}

    def insertRow(self, name: str, row: List[str]) -> None:
        table = self.tables[name]
        row_id = table["next_id"]
        table["rows"][row_id] = row
        table["next_id"] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        table = self.tables[name]
        if rowId in table["rows"]:
            del table["rows"][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables[name]
        return table["rows"][rowId][columnId - 1]