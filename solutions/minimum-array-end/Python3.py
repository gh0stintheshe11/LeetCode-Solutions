from math import log
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        x_bin_str = bin(x)[2:]
        no_of_zeros = 0
        set_positions = []
        for i in range(len(x_bin_str)-1, -1, -1):
            if x_bin_str[i] == "1":
                set_positions.append(i)
            else:
                no_of_zeros += 1
        
        no_of_bits = int(log(n-1, 2))
        starting_number = pow(2, no_of_bits)

        delta = (n-1) - starting_number 
        bin_starting_number = bin(starting_number)[2:]
        rhs = ''
        lhs = bin_starting_number
        if delta:
            rhs = bin(delta)[2:]
            lhs = bin_starting_number[:len(bin_starting_number)-len(rhs)]
        to_merge = lhs + rhs
        if len(to_merge) > no_of_zeros:
            diff = len(to_merge) - no_of_zeros
            x_bin_str = ('0'* diff) + x_bin_str
        
        ptr = len(x_bin_str) -1
        x_bin_list = list(x_bin_str)

        for i in range(len(to_merge)-1, -1, -1):
            while(ptr >=0 and x_bin_list[ptr] != '0'):
                ptr -=1 
            if to_merge[i] == '1':
                x_bin_list[ptr] = '1'
            ptr -=1 
        
        return int(''.join(x_bin_list) , 2)