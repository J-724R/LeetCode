function twoSum(nums: number[], target: number): number[] | void {
  const hashTable: any = {}

  // Equivalent of python enumerate()
  for (const [index, value] of nums.entries()) {
    const difference = target - value
    
    if (difference in hashTable) {
      console.log([hashTable[difference], index])
      return [hashTable[difference], index]
    }
    
    hashTable[value] = index;

    console.log(`${index}: ${value}`);
  }

  return console.error(`Out of reach, invalid target`);
};

twoSum([3, 2, 4], 6)