class Solution:
    def checkInclusion(self, pattern: str, s: str) -> bool:

        letters1 = [0] * 128
        letters2 = [0] * 128
        
        start = 0
        end = len(pattern)
        
        for letter in s[start:end]:
            letters1[ord(letter)] += 1
        
        for letter in pattern:
            letters2[ord(letter)] += 1
        
        print(letters1,letters2)
        
        while end <= len(s):
            if letters1 == letters2:
                return True
            elif end == len(s):
                break
            letters1[ord(s[start])] -= 1
            letters1[ord(s[end])] += 1
            start += 1
            end += 1

        return False