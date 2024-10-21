class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:

        def helper(arr, brr):
            target = ord(arr.pop()[0]) - 1
            while brr and ord(brr[-1][0]) >= target:
                brr.pop()

        while a and b:
            if b[-1] > a[-1]:
                helper(b, a)
                res = False
            else:
                helper(a, b)
                res = True

        return res