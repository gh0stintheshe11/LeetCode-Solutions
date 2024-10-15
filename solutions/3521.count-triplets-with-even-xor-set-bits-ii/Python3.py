class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_set_bits(x):
            return bin(x).count('1')
        
        def count_even_odd(arr):
            even = odd = 0
            for num in arr:
                if count_set_bits(num) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            return even, odd

        a_even, a_odd = count_even_odd(a)
        b_even, b_odd = count_even_odd(b)
        c_even, c_odd = count_even_odd(c)

        even_triplets = (a_even * b_even * c_even) + (a_odd * b_odd * c_even) + (a_even * b_odd * c_odd) + (a_odd * b_even * c_odd)

        return even_triplets