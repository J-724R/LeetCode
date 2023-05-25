class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []
        for num in range((len(nums))//2):
            r.append(nums[num])
            r.append(nums[num + n])
        return r
            

# Faster solution (twice as fast)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []
        for i in range(n):
            r.extend([nums[i], nums[i+n]])
        return r
            