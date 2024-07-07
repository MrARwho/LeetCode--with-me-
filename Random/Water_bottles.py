class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        remain = numBottles
        drink=numBottles

        while(remain >= numExchange):
            x = remain//numExchange
           
            y = remain % numExchange
         
            remain = (x+y)
            
            drink += x
            
        
        return drink

a =Solution()

print(a.numWaterBottles(9,3))
