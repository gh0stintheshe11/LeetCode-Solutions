class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        color_abc = 6  # RGB, RBG, GRB, GBR, BRG, BGR
        color_aba = 6  # RGR, RBR, GYG, GYG, BGB, BRB

        for _ in range(n - 1):
            new_color_abc = (2 * color_abc + 2 * color_aba) % MOD
            new_color_aba = (2 * color_abc + 3 * color_aba) % MOD
            color_abc, color_aba = new_color_abc, new_color_aba

        return (color_abc + color_aba) % MOD