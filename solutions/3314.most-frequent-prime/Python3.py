from typing import List, Tuple
from collections import defaultdict
from itertools import permutations

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        m, n = len(mat), len(mat[0])
        
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        def generate_numbers_from_cell(i: int, j: int, direction: Tuple[int, int]) -> List[int]:
            x, y = i, j
            num = 0
            numbers = []
            while 0 <= x < m and 0 <= y < n:
                num = num * 10 + mat[x][y]
                if num > 10:
                    numbers.append(num)
                x += direction[0]
                y += direction[1]
            return numbers
        
        prime_count = defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                for d in directions:
                    numbers = generate_numbers_from_cell(i, j, d)
                    for number in numbers:
                        if is_prime(number):
                            prime_count[number] += 1
        
        if not prime_count:
            return -1

        most_frequent_prime = -1
        max_count = 0
        
        for prime, count in prime_count.items():
            if count > max_count or (count == max_count and prime > most_frequent_prime):
                most_frequent_prime = prime
                max_count = count
        
        return most_frequent_prime