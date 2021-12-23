class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # A defaultdict without the default dict
        chars = [0] * 128
        
        # Double assignment
        left = right = 0

        # Holding the result
        res = 0
        
        # Until we reach the end
        while right < len(s):
            
            # Convert number to string
            r = s[right]
            
            # Convert string to ASCII value number and add it by 1
            chars[ord(r)] += 1

            # If you notice that the number is greater than 1
            while chars[ord(r)] > 1:
                # Convert left number to string
                l = s[left]
                # Lower its frequency
                chars[ord(l)] -= 1
                # Move the pointer forward
                left += 1

            # ADD 1 TO TAKE INTO ACCOUNT THE ACTUAL LETTERS (SINCE IT STARTS FROM 0)
            res = max(res, right - left + 1)
            
            # Move forward
            right += 1
        
        return res