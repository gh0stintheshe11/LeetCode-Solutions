class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        start_of_week_money = 1
        current_day_money = 1

        for day in range(1, n + 1):
            total_money += current_day_money
            current_day_money += 1

            if day % 7 == 0:
                start_of_week_money += 1
                current_day_money = start_of_week_money

        return total_money