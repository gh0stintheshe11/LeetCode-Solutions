class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1:
            return "9" * n
        if k == 2:
            if n >= 2:
                return "8" + "9" * (n - 2) + "8"
            else:
                return "8"
        if k == 3:
            return "9" * n
        if k == 4:
            if n >= 4:
                return "88" + "9" * (n - 4) + "88"
            else:
                return "8" * n
        if k == 5:
            if n >= 2:
                return "5" + "9" * (n - 2) + "5"
            else:
                return "5"
        if k == 6:
            if n % 2 == 1:
                if n >= 3:
                    return "8" + "9" * (n // 2 - 1) + "8" + "9" * (n // 2 - 1) + "8"
                else:
                    return "6"
            else:
                if n >= 4:
                    return "8" + "9" * (n // 2 - 2) + "77" + "9" * (n // 2 - 2) + "8"
                else:
                    return "66"
        if k == 7:
            if n % 12 == 1 or n % 12 == 5:
                return (n // 2) * "9" + "7" + (n // 2) * "9"
            if n % 12 == 2 or n % 12 == 4:
                return  (n // 2 - 1) * "9" + "77" + (n // 2 - 1) * "9"
            if n % 12 == 3:
                return (n // 2) * "9" + "5" + (n // 2) * "9"
            if n % 12 == 6 or n % 12 == 0:
                return "9" * n
            if n % 12 == 7 or n % 12 == 11:
                return (n // 2) * "9" + "4" + (n // 2) * "9"
            if n % 12 == 8 or n % 12 == 10:
                return (n // 2 - 1) * "9" + "44" + (n // 2 - 1) * "9"
            if n % 12 == 9:
                return (n // 2) * "9" + "6" + (n // 2) * "9"
        if k == 8:
            if n >= 6:
                return "888" + "9" * (n - 6) + "888"
            else:
                return "8" * n
        if k == 9:
            return "9" * n