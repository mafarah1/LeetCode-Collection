class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            if (arr[i]*2) in arr and arr.index(arr[i]*2) != i: #Because i could equal to j, if we're dealing with "0"
                return True