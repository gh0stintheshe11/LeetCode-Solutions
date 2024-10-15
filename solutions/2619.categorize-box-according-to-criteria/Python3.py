class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = (length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9)
        heavy = (mass >= 100)
        
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"