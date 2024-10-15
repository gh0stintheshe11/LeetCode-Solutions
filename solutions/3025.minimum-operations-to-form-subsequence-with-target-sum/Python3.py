class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        powers_of_two = [0] * 31
        for num in nums:
            powers_of_two[num.bit_length() - 1] += 1

        operations = 0
        for i in range(31):
            if target & (1 << i):
                if powers_of_two[i] > 0:
                    powers_of_two[i] -= 1
                else:
                    k = i
                    while k < 31 and powers_of_two[k] == 0:
                        k += 1
                    if k == 31:
                        return -1
                    operations += k - i
                    powers_of_two[k] -= 1
                    for j in range(k - 1, i - 1, -1):
                        powers_of_two[j] += 1

            if i < 30:
                powers_of_two[i + 1] += powers_of_two[i] // 2

        return operations