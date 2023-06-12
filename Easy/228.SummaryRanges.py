# Solution by techwired8
class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]

        # Handle the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(nums[-1]))

        return ranges

# Way faster solution by PratikSen07, beats 80%
class Solution(object):
    def summaryRanges(self, nums):
        output = []
        idx = 0
        while idx < len(nums):
            beg = nums[idx]
            while idx+1 < len(nums) and nums[idx+1] == nums[idx] + 1:
                idx += 1
            last = nums[idx]
            if beg == last:
                output.append(str(beg))
            else:
                output.append(str(beg) + "->" + str(last))
            idx += 1
        return output; 