# My solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        pairs = 0
        for n in nums:
            freq[n] = freq[n] + 1
            if freq[n] > 1:
                pairs += 1
        return pairs


#  Solution with quadratic sequence formula by Skywalker5423
class Solution:
	def numIdenticalPairs(self, nums: List[int]) -> int:
		nums, memo = sorted(nums), {} 
		for i in range(len(nums)-1): 
			if nums[i] == nums[i+1]:
				if nums[i] not in memo:
					memo[nums[i]] = 1
				memo[nums[i]] = memo[nums[i]] + 1 
	
		answer = 0
		for n in memo.values(): 
			answer += (n**2 - n)//2 

		return answer