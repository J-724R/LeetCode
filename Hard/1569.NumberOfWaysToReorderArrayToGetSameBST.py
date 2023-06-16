# Solution by Obose, beats 83.72%
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(nums):
            if len(nums) <= 2: return 1
            left = [n for n in nums if n < nums[0]]
            right = [n for n in nums if n > nums[0]]
            return comb(len(nums) - 1, len(left)) * dfs(left) * dfs(right)
        return (dfs(nums) - 1) % (10 ** 9 + 7)