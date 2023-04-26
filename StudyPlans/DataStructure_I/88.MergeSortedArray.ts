// Bubble sort
function bubbleSort(arr: number[]){
  // grab fisrt index
  // Compare with other and save max
  // Put max at the end of the Array
  // Repeat with index - 1 until everything is sorted
  const size = arr.length

  function recursiveBubbleSort(arr: number[], size: number){
    size -= 1
    if (size == 1) return arr

    let temp: number
    for (let i = 0; i < size; i++) {
      if(arr[i] > arr[i + 1]){
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i+1] = temp
      }
    }
    console.log(`${arr}`);
    recursiveBubbleSort(arr, size)
  }

  console.log(`${arr}`);
  return recursiveBubbleSort(arr, size)
}

bubbleSort([4, 7, 8, 1, 9, 2, 3, 15, 1])


function LeetCodeMerge(nums1: number[], m: number, nums2: number[], n: number): void {
  function recursiveBubbleSort(arr: number[], size: number){
    size -= 1
    if (size == 1) return arr

    let temp: number
    for (let i = 0; i < size; i++) {
    if(arr[i] > arr[i + 1]){
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i+1] = temp
    }
    }
    console.log(`${arr}`);
    recursiveBubbleSort(arr, size)
  }

  const sorted1 = recursiveBubbleSort(nums1, m);
  const sorted2 = recursiveBubbleSort(nums2, n);

  nums1 = sorted1.concat(sorted2)
};

// from python code
function mergeV2merge(nums1: number[], m: number, nums2: number[], n: number): void {
  while (n > 0) {
    if((m <= 0) || (nums2[n-1] >= nums1[m-1] )){
      nums1[m+n-1] = nums2[n-1]
      n -= 1
    } else {
      nums1[m+n-1] = nums1[m-1]
      m -= 1
    }
  }
}