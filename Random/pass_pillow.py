from typing import List
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        
        curr = 1
        rev = 0
        for i in range(0,time):
            # print(i)
            # print("curr",curr)
            if (rev == 1):
                # print("rev =1")
                if(curr == 1):
                    rev = 0
                    curr = curr+1
                else:
                    curr = curr -1  
            else:
                # print("rev = 0")
                if(curr == n):
                    # print("cuu = n")
                    rev = 1
                    curr = curr - 1 
                else:
                    curr = curr+1
                    # print("curr ",curr)
        return curr
        
a = Solution()   
print(a.passThePillow(18,38))
        
        