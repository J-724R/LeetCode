# Learning enumerate loop
def twoSum(nums):
  for index, value in enumerate(nums):
    print(index, value)    

twoSum([2,7,11,15])

import json

class Solution:
  def twoSum(nums, target):
    hashTable = {}
    for index, value in enumerate(nums):
      hashTable[value] = index
      diference = target - value
      if diference in hashTable:
        return print([hashTable[diference], index])
    
    print(json.dumps(hashTable, indent=4))

  twoSum([2,7,11,15], 9)