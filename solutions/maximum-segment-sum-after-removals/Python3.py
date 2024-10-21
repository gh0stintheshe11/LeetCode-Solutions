class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        ret = [0] 
        curr_max = 0
        dct = {}
        for index in removeQueries[:0:-1]:
            temp = nums[index]
            lower_index = upper_index = index

            if index - 1 in dct:
                temp += dct[index-1][0]
                lower_index = dct[index-1][1][0]
            
            if index + 1 in dct:
                temp += dct[index+1][0]
                upper_index = dct[index+1][1][1]
                
            dct[lower_index] = (temp, (lower_index, upper_index))
            dct[upper_index] = (temp, (lower_index, upper_index))
            curr_max = max(curr_max, temp)
            ret.append(curr_max)
        return ret[::-1]