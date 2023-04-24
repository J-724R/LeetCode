class Solution:
  def containsDuplicate(self, nums) -> bool:
    numsSet = set(nums)
    return True if numsSet != len(nums) else False
  

