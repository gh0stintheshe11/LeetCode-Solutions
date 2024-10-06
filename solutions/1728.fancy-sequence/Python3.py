class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.sequence = []
        self.add = 0
        self.mul = 1
        
    def append(self, val: int) -> None:
        # To maintain cumulative effects, apply the reverse transformation
        val = (val - self.add) * pow(self.mul, self.MOD-2, self.MOD) % self.MOD
        self.sequence.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.MOD
        self.mul = self.mul * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        return (self.sequence[idx] * self.mul + self.add) % self.MOD