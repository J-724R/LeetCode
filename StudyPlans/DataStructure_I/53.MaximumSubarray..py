import math

class Solution:
  def maxSubArray(self, nums) -> int:
    maxSum = -math.inf

    for i in range(len(nums)):
      currentSum = 0
      for j in range(len(nums)):
        currentSum += nums[j]
        maxSum = max(maxSum, currentSum)
  
    return maxSum

