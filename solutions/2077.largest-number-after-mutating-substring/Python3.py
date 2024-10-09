class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num_list = list(num)
        mutated = False
        for i in range(len(num_list)):
            current_digit = int(num_list[i])
            if change[current_digit] > current_digit:
                num_list[i] = str(change[current_digit])
                mutated = True
            elif change[current_digit] < current_digit and mutated:
                break
        return "".join(num_list)