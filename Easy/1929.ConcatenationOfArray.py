class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        n = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[n+i] = nums[i]
        return ans