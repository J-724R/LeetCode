function twoSum(nums: number[], target: number): number[] | void {
  const hashTable: any = {}

  // Equivalent of python enumerate()
  for (const [index, value] of nums.entries()) {
    hashTable[value] = index;

    const difference = target - value

    if (difference in hashTable) {
      console.log([hashTable[difference], index])
      return [hashTable[difference], index]
    }
    
    console.log(`${index}: ${value}`);
  }

  return console.error(`Out of reach, invalid target`);
};

twoSum([1, 4, 5, 6, 7, 10, 1], 16)