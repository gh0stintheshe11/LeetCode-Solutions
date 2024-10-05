class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def generate_strobogrammatic(n, total_len):
            if n == 0: return [""]
            if n == 1: return ["0", "1", "8"]
            prev = generate_strobogrammatic(n - 2, total_len)
            res = []
            for num in prev:
                if n != total_len:
                    res.append("0" + num + "0")
                res.append("1" + num + "1")
                res.append("6" + num + "9")
                res.append("8" + num + "8")
                res.append("9" + num + "6")
            return res
        
        def is_valid(num, low, high):
            if len(num) > 1 and num[0] == '0':
                return False
            if len(num) < len(low) or len(num) > len(high):
                return False
            if len(num) == len(low) and num < low:
                return False
            if len(num) == len(high) and num > high:
                return False
            return True

        count = 0
        for length in range(len(low), len(high) + 1):
            nums = generate_strobogrammatic(length, length)
            for num in nums:
                if is_valid(num, low, high):
                    count += 1
        return count