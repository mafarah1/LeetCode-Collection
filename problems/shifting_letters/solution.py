class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans, shift = '', 0
        for i in range(len(shifts) -1, -1, -1):
            ans += chr((ord(s[i]) - ord('a') + shift+shifts[i]) % 26 + ord('a')) # He found a formula for figuring out the characters
            shift += shifts[i]
        
        return ans[::-1]

# # Function for "shifting" individually

# def shift(string, number):
#     for i in range(number):
#         string[i]

# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        