class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        max_distance = self.seats[0]
        pos = 0
        for i in range(len(self.seats) - 1):
            distance = (self.seats[i+1] - self.seats[i]) // 2
            if distance > max_distance:
                max_distance = distance
                pos = self.seats[i] + distance
        if self.n - 1 - self.seats[-1] > max_distance:
            pos = self.n - 1
        self.seats.append(pos)
        self.seats.sort()
        return pos

    def leave(self, p: int) -> None:
        self.seats.remove(p)