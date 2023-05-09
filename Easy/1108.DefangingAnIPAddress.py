class Solution:
    def defangIPaddr(self, address: str) -> str:
      res = ""

      for i in address:
        if i == ".":
          res += "[.]"
        else:
          res += i 
      return res

class BuiltInsSolutions:
    def defangIPaddr(self, address: str) -> str:
      return address.replace('.', "[.]")
    def defangIPaddrII(self, address: str) -> str:
      return '[.]'.join(address.split('.'))
    # Fastest One
    def defangIPaddrIII(self, address: str) -> str:
      return re.sub('\.', '[.]', address)




# Intutions
# Use built in methods
# replace
# traverse strng an replace to [.]