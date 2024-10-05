from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings
        nums_str = list(map(str, nums))
        
        # Define a comparator that compares two strings based on their concatenated result
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort the list using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted list into a single string
        largest_num = ''.join(nums_str)
        
        # Edge case: if the largest number is '0', return '0'
        if largest_num[0] == '0':
            return '0'
        
        return largest_num