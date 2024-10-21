class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))
        self.used = set()

    def get(self) -> int:
        if self.available:
            number = self.available.pop()
            self.used.add(number)
            return number
        return -1

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.available.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)