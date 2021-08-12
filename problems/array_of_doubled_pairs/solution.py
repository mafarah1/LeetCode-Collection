import collections

def checkDuplicates(arr: List[int]) -> bool:
    return len(arr) != len(set(arr))

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True