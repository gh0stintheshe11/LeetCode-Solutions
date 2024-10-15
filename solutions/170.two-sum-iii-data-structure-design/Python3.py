class TwoSum:

    def __init__(self):
        self.numbers = {}
        
    def add(self, number: int) -> None:
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1

    def find(self, value: int) -> bool:
        for num in self.numbers:
            complement = value - num
            if complement in self.numbers:
                if complement != num or self.numbers[complement] > 1:
                    return True
        return False