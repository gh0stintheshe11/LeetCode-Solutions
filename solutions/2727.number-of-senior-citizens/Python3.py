from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            # Extract the age part from the string
            age_str = detail[11:13]
            # Convert the age part to an integer
            age = int(age_str)
            # Check if the age is greater than 60
            if age > 60:
                count += 1
        return count