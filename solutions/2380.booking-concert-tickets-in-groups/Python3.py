from collections import defaultdict

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.row_seats = defaultdict(lambda: 0)
        self.min_row = defaultdict(lambda: 0)
        self.m = m
        self.total_remaining = m * n
        self.seen = set()

    def min_row_seats(self, k, maxRow): # minimum row with at least k seats
        mr = self.min_row[k]
        for i in range(mr, maxRow + 1):
            if self.row_seats[i] <= self.m - k:
                self.min_row[k] = i
                return i
        return -1

    def gather(self, k: int, maxRow: int) -> List[int]:
        if (k, self.total_remaining, "g") in self.seen or self.total_remaining < k:
            return []
        row = self.min_row_seats(k, maxRow)
        if row == -1:
            self.seen.add((k, self.total_remaining, "g"))
            return []
        out = [row, self.row_seats[row]]
        self.row_seats[row] += k
        self.total_remaining -= k
        return out

    def scatter(self, k: int, maxRow: int) -> bool:
        if (k, self.total_remaining, "s") in self.seen or self.total_remaining < k:
            return False
        row = self.min_row_seats(1, maxRow)
        ko = k
        ro = row
        if row == -1:
            self.seen.add((k, self.total_remaining, "s"))
            return False
        while k:
            if row > maxRow:
                self.seen.add((ko, self.total_remaining, "s"))
                return False
            if self.row_seats[row] > self.m - k:
                k -= self.m - self.row_seats[row]
                row += 1
            else:
                break
                
        k = ko
        row = ro
        while k:
            if row > maxRow:
                return False
            if self.row_seats[row] > self.m - k:
                k -= self.m - self.row_seats[row]
                self.row_seats[row] = self.m
                row += 1
            else:
                self.row_seats[row] += k
                break
        self.total_remaining -= ko
        return True