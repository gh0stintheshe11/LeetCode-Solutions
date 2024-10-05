class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.sum += val
        if len(self.window) > self.size:
            self.sum -= self.window.pop(0)
        return self.sum / len(self.window)