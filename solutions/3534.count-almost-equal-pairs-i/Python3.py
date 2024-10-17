class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def is_almost_equal(num1, num2):
            s_num1, s_num2 = str(num1), str(num2)
            while len(s_num1) < len(s_num2):
                s_num1 = '0'+s_num1

            while len(s_num1) > len(s_num2):
                s_num2 = '0'+s_num2

            diff = 0
            idx = []
            for i in range(len(s_num1)):
                if s_num1[i] != s_num2[i]:
                    idx.append(i)
                    diff += 1
                if diff > 2:
                    return False
            if diff == 2:
                list_num1 = list(s_num1)
                list_num1[idx[0]], list_num1[idx[1]] = list_num1[idx[1]], list_num1[idx[0]]
                if ''.join(list_num1) == s_num2:
                    return True
            return False

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] or is_almost_equal(nums[i], nums[j]):
                    ans += 1
        return ans