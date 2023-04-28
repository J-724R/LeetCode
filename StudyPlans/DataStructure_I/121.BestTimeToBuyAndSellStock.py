# find min value and store its index
# if min value is in last index return 0
# sum values after minIndex, find max profit
# return max

import math
# Invalid Solution
class Solution:
    def maxProfit(prices):
      min = math.inf
      minIndex = 0
      max = 0
      
      for i in range(len(prices)):
        if prices[i] < min:
          min = prices[i]
          minIndex = i
        if minIndex == len(prices) - 1: return 0

      for i in range(minIndex, len(prices)):
        if (prices[i] - min) > max:
          max = prices[i] - min 

      return max
    
    print(maxProfit([1,2]))


# Two pointers approach
class SolutionII:
  def maxProfit(self, prices: List[int]) -> int:
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            max_profit =max(currentProfit,max_profit)
        else:
            left = right
        right += 1
    return max_profit

        


         