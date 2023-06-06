class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        l = len(arr) # It's way faster without this line
        dif = arr[1]-arr[0]

        for i in range(2,l):
            if dif != arr[i] - arr[i-1]:
                return False
        return True
    
# faster solution by rock, beats 50%
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i - 2] - arr[i - 1] == arr[i - 1] - arr[i] for i in range(2, len(arr)))