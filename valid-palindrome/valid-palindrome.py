class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        
        #process the string
        s = ''.join(x for x in s if x.isalnum()).lower()
        
        left = 0
        right = len(s) - 1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        