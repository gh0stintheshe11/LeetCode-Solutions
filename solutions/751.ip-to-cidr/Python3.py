class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_int(ip):
            parts = list(map(int, ip.split('.')))
            return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

        def int_to_ip(x):
            return f"{(x >> 24) & 255}.{(x >> 16) & 255}.{(x >> 8) & 255}.{x & 255}"

        def max_cidr_block(start, n):
            mask = 1
            while start & mask == 0 and mask <= n:
                mask <<= 1
            return mask

        start = ip_to_int(ip)
        result = []

        while n > 0:
            size = max_cidr_block(start, n)
            while size > n:
                size >>= 1
            mask_length = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start)}/{mask_length}")
            start += size
            n -= size

        return result