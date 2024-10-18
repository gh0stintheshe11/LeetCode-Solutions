class Solution:
    def maxValue(self, nums, k):
        n = len(nums)
        MAX_OR = 128  # Since nums[i] <= 127

        from collections import defaultdict

        # Initialize dp_forward[i][l]: set of OR values of subsequences of length l ending at index i
        dp_forward = [ [set() for _ in range(k + 1)] for _ in range(n) ]
        # Initialize dp_backward[i][l]: set of OR values of subsequences of length l starting at index i
        dp_backward = [ [set() for _ in range(k + 1)] for _ in range(n) ]

        # Build dp_forward
        for i in range(n):
            num = nums[i]
            dp_forward[i][1].add(num)
            if i > 0:
                for l in range(1, k + 1):
                    # Exclude nums[i]
                    dp_forward[i][l].update(dp_forward[i - 1][l])
                    if l > 1:
                        # Include nums[i]
                        for or_value in dp_forward[i - 1][l - 1]:
                            dp_forward[i][l].add(or_value | num)

        # Build dp_backward
        for i in range(n - 1, -1, -1):
            num = nums[i]
            dp_backward[i][1].add(num)
            if i < n - 1:
                for l in range(1, k + 1):
                    # Exclude nums[i]
                    dp_backward[i][l].update(dp_backward[i + 1][l])
                    if l > 1:
                        # Include nums[i]
                        for or_value in dp_backward[i + 1][l - 1]:
                            dp_backward[i][l].add(or_value | num)

        max_value = 0

        # For each possible split position
        for split in range(n - 1):
            # Ensure enough elements on both sides
            if split >= k - 1 and n - split - 1 >= k:
                or_set1 = dp_forward[split][k]
                or_set2 = dp_backward[split + 1][k]
                for or1 in or_set1:
                    for or2 in or_set2:
                        value = or1 ^ or2
                        if value > max_value:
                            max_value = value

        return max_value
