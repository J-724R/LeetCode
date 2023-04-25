import math

class Solution:
  def maxSubArray(self, nums) -> int:
    maxSum = -math.inf

    for i in range(len(nums)):
      currentSum = 0
      for j in range(i, len(nums)):
        currentSum += nums[j]
        maxSum = max(maxSum, currentSum)
  
    return maxSum

# Dynamic Programing | Memoization
class SolutionII:
    def maxSubArray(self, nums):
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
        return dp[0][-1]
