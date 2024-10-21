class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.size = size
        self.ones_count = 0
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones_count += 1
        else:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones_count += 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones_count -= 1
        else:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones_count -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones_count = self.size - self.ones_count

    def all(self) -> bool:
        return self.ones_count == self.size

    def one(self) -> bool:
        return self.ones_count > 0

    def count(self) -> int:
        return self.ones_count

    def toString(self) -> str:
        if self.flipped:
            return ''.join('1' if bit == 0 else '0' for bit in self.bits)
        else:
            return ''.join(str(bit) for bit in self.bits)