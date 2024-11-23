
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[1]
        
        for i in range(1,len(prices)):
            if (buy > prices[i]):
                buy = prices[i]
            if (sell < prices[i]):
                sell = prices[i]
        if ((sell-buy)>=0):
            return sell-buy
        else:
            return 0
        


        