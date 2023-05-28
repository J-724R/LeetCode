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


