# Solution by sgallivan, beats 85.5% 
class Solution:
    def maxProfit(self, P: List[int], F: int) -> int:
        buying, selling = 0, -P[0]
        for i in range(1, len(P)):
            buying = max(buying, selling + P[i] - F)
            selling = max(selling, buying - P[i])
        return buying