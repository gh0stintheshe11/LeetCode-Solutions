class LUPrefix:

    def __init__(self, n: int):
        self.uploads = [False] * (n + 1)
        self.longest_prefix = 0

    def upload(self, video: int) -> None:
        self.uploads[video] = True
        while self.longest_prefix + 1 < len(self.uploads) and self.uploads[self.longest_prefix + 1]:
            self.longest_prefix += 1

    def longest(self) -> int:
        return self.longest_prefix