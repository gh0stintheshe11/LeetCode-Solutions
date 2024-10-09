from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        current = self.root
        for bit in range(15, -1, -1):
            bit_value = (num >> bit) & 1
            if bit_value not in current.children:
                current.children[bit_value] = TrieNode()
            current = current.children[bit_value]
            current.count += 1

    def count_less_than(self, num, limit):
        current = self.root
        count = 0
        for bit in range(15, -1, -1):
            if current is None:
                break
            limit_bit = (limit >> bit) & 1
            num_bit = (num >> bit) & 1
            if limit_bit == 1:
                if num_bit in current.children:
                    count += current.children[num_bit].count
                current = current.children.get(1 - num_bit, None)
            else:
                current = current.children.get(num_bit, None)
        return count

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def countPairsWithXORLessThan(K: int) -> int:
            trie = Trie()
            count = 0
            for num in nums:
                count += trie.count_less_than(num, K)
                trie.insert(num)
            return count
        
        total_high = countPairsWithXORLessThan(high + 1)
        total_low = countPairsWithXORLessThan(low)
        return total_high - total_low