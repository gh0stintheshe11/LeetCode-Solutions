class Solution:
    def __init__(self):
        self.MOD = 1000000007
        self.memo = {0: 1}
        self.fact = [1 for i in range(10100)]
        
    def inv(self, x):
        if x > 1: return self.inv(self.MOD % x) * (self.MOD - self.MOD // x) % self.MOD 
        else: return x
        
    def choose(self, n, k):
        return ((self.fact[n] * self.inv(self.fact[n-k]) ) % self.MOD) * self.inv(self.fact[k]) % self.MOD
    
    def factors(self, x):
        a = []
        i = 2
        while x > 1:
            re = 0
            while x % i == 0:
                re += 1
                x //= i
            if re: a.append(re)
            i += 1
        return a   
    
    def h(self, v):
        if v in self.memo: return self.memo[v]
        self.memo[v] = self.choose(v + self.c, self.c)
        return self.memo[v]
        
    def idealArrays(self, n: int, maxValue: int) -> int:
        s = 0
        self.c = n - 1
        
        for i in range(2, 10100):
            self.fact[i] = self.fact[i - 1] * i % self.MOD

        for i in range(1, maxValue + 1):
            cur = 1
            fa = self.factors(i)
            for f in fa: cur = (cur * self.h(f)) % self.MOD
            s = (s + cur) % self.MOD
        return s