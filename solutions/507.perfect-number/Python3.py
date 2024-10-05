class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        div_sum = 1
        sq_root = int(num**0.5)
        for i in range(2, sq_root + 1):
            if num % i == 0:
                div_sum += i
                if i != num // i:
                    div_sum += num // i
        return div_sum == num