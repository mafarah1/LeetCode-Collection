class Solution:
    def lengthOfLongestSubstringKDistinct(self, str1: str, k: int) -> int:

        if k == 0:
            return 0

        if len(set(str1)) <= k:
            return len(str1)

        start = 0
        end = 0

        maximum = 0

        while start <= end and end <= len(str1):
            if len(set(str1[start:end])) > k:
                maximum = max(maximum, len(str1[start:end-1]))
                start += 1
                while str1[start] == str1[start-1]:
                  start += 1
            if end == len(str1):
                maximum = max(maximum, len(str1[start:end]))
            end += 1

        return maximum