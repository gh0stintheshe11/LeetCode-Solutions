class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.incrementArray = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        if index > 0:
            self.incrementArray[index - 1] += self.incrementArray[index]
        result = self.stack.pop() + self.incrementArray[index]
        self.incrementArray[index] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.incrementArray[min(k, len(self.stack)) - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)