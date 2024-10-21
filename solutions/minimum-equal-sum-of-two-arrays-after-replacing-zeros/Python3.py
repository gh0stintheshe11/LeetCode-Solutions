class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_cnt_1, zero_cnt_2 = 0, 0
        sum_1, sum_2 = 0, 0
        for num in nums1:
            if num == 0:
                zero_cnt_1 += 1
            else:
                sum_1 += num

        for num in nums2:
            if num == 0:
                zero_cnt_2 += 1
            else:
                sum_2 += num

        sum_1 += zero_cnt_1
        sum_2 += zero_cnt_2
        if sum_1 > sum_2 and zero_cnt_2 == 0:
            return -1

        if sum_2 > sum_1 and zero_cnt_1 == 0:
            return -1

        return max(sum_1, sum_2)