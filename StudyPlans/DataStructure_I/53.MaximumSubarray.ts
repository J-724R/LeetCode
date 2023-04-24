// Brute Force | Trying out every possible sub-array in nums
function maxSubArray(nums: number[]): number {
  let maxSum = -Infinity

  for (let i = 0; i < nums.length; i++) {
    let currentSum = 0
      for (let j = i; j < nums.length; j++) {
        currentSum += nums[j] 
        maxSum = Math.max(maxSum, currentSum)
      }
  }

  return maxSum
};

console.log(maxSubArray([1,2.-7,5,-3,6,1,3,-100]));