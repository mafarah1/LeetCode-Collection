import collections

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq_b = collections.Counter(nums)
        freq = freq_b.items()
        i = 0
        for key, value in freq:
            if value > 1:
                while i < (value-1):
                    nums.remove(key)
                    i += 1
                i = 0
        return len(nums)