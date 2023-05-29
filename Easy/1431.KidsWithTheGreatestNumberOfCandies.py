class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies) - extraCandies
        return [x >= max_ for x in candies]
    

# Beats 93% by mybuddy29
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy+extraCandies >= maxCandies for candy in candies]
        