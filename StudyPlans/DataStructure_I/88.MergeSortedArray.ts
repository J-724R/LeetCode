// Bubble sort
function bubbleSort(arr: number[]){
  // grab fisrt index
  // Compare with other and save max
  // Put max at the end of the Array
  // Repeat with index - 1 until everything is sorted
  const size = arr.length

  function recursiveBubbleSort(arr: number[], size: number){
    size -= 1
    if (size == 0) return arr

    let temp: number
    for (let i = 0; i < size; i++) {
      if(arr[i] > arr[i + 1]){
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i+1] = temp
      }
    }
    console.log(arr);
    recursiveBubbleSort(arr, size)
  }

  return recursiveBubbleSort(arr, size)
}

bubbleSort([4, 7, 8, 1, 9, 2])

function LeetCodeMerge(nums1: number[], m: number, nums2: number[], n: number): void {
    
};