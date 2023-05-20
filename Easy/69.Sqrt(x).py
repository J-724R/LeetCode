# Easy sol with built in methods
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))
    

# one of intended solutions | Binary Search
public int sqrt(int x) {
    if (x == 0)
        return 0;
    int left = 1, right = Integer.MAX_VALUE;
    while (true) {
        int mid = left + (right - left)/2;
        if (mid > x/mid) {
            right = mid - 1;
        } else {
            if (mid + 1 > x/(mid + 1))
                return mid;
            left = mid + 1;
        }
    }
}

# in python l, r = 0, x
class SolutionBinarySearch:
    def mySqrt(self, x: int) -> int:
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1

# Newtons iterative method
class SolutionNewton:
    def mySqrt(self, x: int) -> int:
      r = x + 1  # avoid dividing 0
      while r*r > x:
              r = int(r - (r*r - x)/(2*r))  # newton's method
      return r