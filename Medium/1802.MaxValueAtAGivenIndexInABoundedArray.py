# solution by techwired8
class Solution:
    def check(self, a):
        left_offset = max(a - self.index, 0)
        result = (a + left_offset) * (a - left_offset + 1) // 2
        right_offset = max(a - ((self.n - 1) - self.index), 0)
        result += (a + right_offset) * (a - right_offset + 1) // 2
        return result - a

    def maxValue(self, n, index, maxSum):
        self.n = n
        self.index = index

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        result = left + 1
        return result
    
# Math solution by louis925, beats 66.41%
import math
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n              # remove the contributions from all the 1 in each element.
		                         # We will add 1 back to the final height later
        if index < n // 2:       # make the index closer to the right boundary
            index = n - index - 1
        n_left = index           # number of element to the left of the index
        n_right = n - 1 - index  # number of element to the right of the index
        tri_left = (n_left * (n_left + 1)) // 2     # the triangle area for the left side if not hitting the boundary
        tri_right = (n_right * (n_right + 1)) // 2  # the triangle area for the right side if not hitting the boundary
		# case 1: perfect pyramid
        if maxSum <= (tri_right * 2 + n_right + 1):
            return int(math.sqrt(maxSum)) + 1
		# case 2: right side hits the boundary
        if maxSum <= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1):
            b = 3 + 2 * n_right
            return int((-b + math.sqrt(b * b - 8 * (tri_right + 1 - n_right * n_right - maxSum))) / 2) + 1 + 1
		# case 3: both sides hit boundaries
        maxSum -= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1)
        return n_left + 1 + 1 + (maxSum // n)