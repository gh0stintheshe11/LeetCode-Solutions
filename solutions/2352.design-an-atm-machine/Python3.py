class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.counts = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        to_withdraw = [0] * 5
        for i in range(4, -1, -1):
            num_notes = min(self.counts[i], amount // self.denominations[i])
            to_withdraw[i] = num_notes
            amount -= num_notes * self.denominations[i]

        if amount == 0:
            for i in range(5):
                self.counts[i] -= to_withdraw[i]
            return to_withdraw
        else:
            return [-1]