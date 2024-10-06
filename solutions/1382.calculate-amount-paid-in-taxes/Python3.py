class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        previous_upper = 0
        for upper, percent in brackets:
            if income > previous_upper:
                taxable_income = min(income, upper) - previous_upper
                tax += taxable_income * (percent / 100)
            previous_upper = upper
        return tax