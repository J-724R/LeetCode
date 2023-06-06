class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        l = len(arr)
        dif = arr[1]-arr[0]

        for i in range(2,l):
            if dif != arr[i] - arr[i-1]:
                return False
        return True