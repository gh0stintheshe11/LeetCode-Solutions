class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emp=0
        ans=numBottles
    
        emp=numBottles
        numBottles=0
        while numBottles!=0 or numExchange<=emp:
            emp-=numExchange
            numExchange+=1
            numBottles+=1
            
            while numBottles!=0:
                ans+=1
                numBottles-=1
                emp+=1
                         
        return ans