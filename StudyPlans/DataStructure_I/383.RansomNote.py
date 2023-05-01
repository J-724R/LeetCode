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
    
    print(canConstruct('strings', 'strings', 'strings'))
