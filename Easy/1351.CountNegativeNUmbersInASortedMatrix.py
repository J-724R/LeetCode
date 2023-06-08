class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for arr in grid:
            for n in arr:
                if n < 0:
                    res += 1
        return res