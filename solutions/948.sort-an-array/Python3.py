
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums):
            if len(nums)>1:
                mid=len(nums)//2
                left_list=nums[:mid]
                right_list=nums[mid:]
                merge(left_list)
                merge(right_list)
                a,b,c=0,0,0
                while a<len(left_list) and b<len(right_list):
                    if left_list[a]<right_list[b]:
                        nums[c]=left_list[a]
                        a+=1
                        c+=1
                    else:
                        nums[c]=right_list[b]
                        b+=1
                        c+=1
                while a<len(left_list):
                    nums[c]=left_list[a]
                    a+=1
                    c+=1
                while b<len(right_list):
                    nums[c]=right_list[b]
                    b+=1
                    c+=1
        merge(nums)
        return nums
