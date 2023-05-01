from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      hashmap = {}
      for i in magazine:
        print(i)
        if i not in hashmap:
          hashmap[i] = 1
        else:
          hashmap[i] += 1
      for i in range(len(ransomNote)):
        if hashmap[ransomNote[i]] >= 0: 
          hashmap[ransomNote[i]] -= 1
        else: return False
      return True
    
    # using counter
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
      st1, st2 = Counter(ransomNote), Counter(magazine)
      if st1 & st2 == st1:
          return True
      return False