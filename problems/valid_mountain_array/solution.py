class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        j = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1] and i == 1:
                return False
            if arr[i] <= arr[i-1]:
                j = i
                break
        for i in range(j, len(arr)):
            if arr[i] >= arr[i-1]:
                return False
        return True