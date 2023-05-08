class Solution:
    def longestCommonPrefix(self, strs):
      res = ""

      for i in range(len(strs[0])):
        for s in strs:
          if i == len(s) or s[i] != strs[0][i]:
            return res
        res += strs[0][i]

      return res 

# intuition, tow pointers aproach

# grab first string, 
# compare each char with the rest of the string

# stop loop when finding different char or a string gets out of bounds

# more eficient solution

class SolutionII:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if strs == None: return ""
      if len(strs) == 1: return strs[0]

      strs.sort(0)
      prefix = ""
      for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
          prefix += strs[0][i]
        else:
          break
           
      return prefix