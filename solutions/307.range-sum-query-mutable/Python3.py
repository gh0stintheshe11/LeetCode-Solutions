class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n * 4)
        self.build_tree(0, 0, self.n - 1)
        
    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build_tree(left_child, start, mid)
            self.build_tree(right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index: int, val: int) -> None:
        self.update_tree(0, 0, self.n - 1, index, val)
        
    def update_tree(self, node, start, end, idx, val):
        if start == end:
            self.nums[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update_tree(left_child, start, mid, idx, val)
            else:
                self.update_tree(right_child, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_tree(0, 0, self.n - 1, left, right)
        
    def sum_tree(self, node, start, end, L, R):
        if R < start or L > end:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.sum_tree(left_child, start, mid, L, R)
        right_sum = self.sum_tree(right_child, mid + 1, end, L, R)
        return left_sum + right_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)