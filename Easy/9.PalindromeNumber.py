# Most straight foward solution
class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False
    
    return str(x) == str(x)[::-1]  
  
# It's even faster than build in method reverse string
class SolutionII:
  def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x > 0 and x%10 == 0):
      return False
    
    result = 0
    while x > result:
      print(f"x = {x}")
      print(f"{result * 10} + {x % 10} = {result * 10 + x % 10}")
      result = result * 10 + x % 10
      x = x // 10
      
    return True if (x == result or x == result // 10) else False

  isPalindrome(2, 123551645367)
   


# Proper solution within rules
# check if >0
# if pair middle number has to be equal
# if inpair middle have to be unique and middle -1, middle + 1 have to be equal
# campare each side after conditions
