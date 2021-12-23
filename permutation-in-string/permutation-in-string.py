class Solution:
    def checkInclusion(self, pattern: str, s: str) -> bool:
        import collections

        start = 0
        end = len(pattern)
        res = False

        while end <= len(s):
            if collections.Counter(s[start:end]) == collections.Counter(pattern):
                return True
            start += 1
            end += 1

        return False