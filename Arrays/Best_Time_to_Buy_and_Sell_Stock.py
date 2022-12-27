
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0

        # for i in range(1,len(prices)):
        #     if prices[i] > prices[i-1]:
        #         profit += prices[i] - prices[i-1]
        # return profit 
        # maxprofit = 0
        # minpurchase = prices[0]
        # for i in range(1,len(prices)):
        #     maxprofit = max(maxprofit,prices[i]-minpurchase)
        #     minpurchase = min(minpurchase,prices[i])
        # return maxprofit



        # n = len(prices)
        # if n < 2:
        #     return 0
        
        # maxprofit = 0
        # i = 0 

        # while i < n-1:

        #     #finding local  minima
        #     while i < n-1 and prices[i+1] <= prices[i]:
        #         i+=1
        #     buy = i
            

        #     if i == n-1:
        #         break

        #     #finding local maxima
        #     while i < n-1 and prices[i+1] >= prices[i]:
        #         i+=1
        #     sell = i
        #     maxprofit += prices[sell] - prices[buy]

        # return maxprofit

        l  = []

        for i in range(len(prices)-1):

            if prices[i] < prices[i+1]:
                l.append(prices[i+1] - prices[i])
        return sum(l)            


prices = [1,2,3,4,5]
solution = Solution()
print(solution.maxProfit(prices))