class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dic = {}
        ans = 1

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        if 1 in dic:
            if dic[1] % 2 == 0:
                ans = max(ans, dic[1] - 1)
            else:
                ans = max(ans, dic[1])
            
            dic.pop(1)

        for key, value in dic.items():
            if value >= 2:
                temp = 2
                tempNum = key
                tempNum = tempNum ** 2
                while tempNum in dic:
                    if dic[tempNum] == 1:
                        temp += 1
                        break
                    elif dic[tempNum] >= 2:
                        temp += 2
                        ans = max(ans, temp-1)
                    
                    tempNum = tempNum ** 2
                if temp % 2 != 0:
                    ans = max(ans, temp)
        
        return ans