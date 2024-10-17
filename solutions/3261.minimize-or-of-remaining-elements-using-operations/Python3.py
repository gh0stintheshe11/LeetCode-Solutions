class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        def same_prefix(mask, prefix, p):
            # check if all 0-bits in prefix are also 0 in mask. Ignore lower p bits.
            mask, prefix = mask >> p, prefix >> p
            return mask | prefix == prefix
        
        n = len(nums)
        M = max(len(bin(v))-2 for v in nums)
        full_mask = (1 << M) - 1
        prefix = 0
        for p in range(M-1, -1, -1):
            cnt = 0
            block_res = full_mask
            block_size = 0
            for v in nums:
                if not same_prefix(v, prefix, p):
                    block_res &= v
                    block_size += 1
                    if same_prefix(block_res, prefix, p):
                        cnt += block_size - 1
                        block_res, block_size = full_mask, 0
                else:
                    cnt += block_size
                    block_res, block_size = full_mask, 0
            if block_size: # last block if it's not already processed
                cnt += block_size
            if cnt > k:
                prefix ^= 1 << p
        return prefix