class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        sum = 0
        for n in gain:
            sum += n
            if sum >= max:
                max= sum
        return max 