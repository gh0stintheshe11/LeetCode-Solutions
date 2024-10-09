class MRUQueue:

    def __init__(self, n: int):
        self.queue = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        value = self.queue.pop(k - 1)
        self.queue.append(value)
        return value