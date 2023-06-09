class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for arr in grid:
            for n in arr:
                if n < 0:
                    res += 1
        return res
    

# Solved with binary Search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        currRowNegativeIndex = n - 1

        # Iterate on all rows of the matrix one by one.
        for row in grid:
            # Decrease 'currRowNegativeIndex' so that it points to current row's last positive element.
            while currRowNegativeIndex >= 0 and row[currRowNegativeIndex] < 0:
                currRowNegativeIndex -= 1
            # 'currRowNegativeIndex' points to the last positive element,
            # which means 'n - (currRowNegativeIndex + 1)' is the number of all negative elements.
            count += (n - (currRowNegativeIndex + 1))
        return count
    
# Better explained Solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        # Iterate on all rows of the matrix one by one.
        for row in grid:
            # Using binary search find the index
            # which has the first negative element.
            left, right = 0, n - 1
            while left <= right:
                mid = (right + left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            # 'left' points to the first negative element,
            # which means 'n - left' is the number of all negative elements.
            count += (n - left)
        return count