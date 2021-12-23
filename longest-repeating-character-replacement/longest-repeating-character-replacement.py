class Solution:
    def characterReplacement(self, str1: str, k: int) -> int:
        # Defualtdict without the defaultdict
        letters = [0] * 128

        left = right = 0

        res = 0

        maxRepeatLetter = 0

        while right < len(str1):

            r = str1[right]

            letters[ord(r)] += 1

            maxRepeatLetter = letters.index(max(letters))

            if sum(letters) - letters[maxRepeatLetter] > k and letters[maxRepeatLetter] != 0:
                l = str1[left]
                left += 1
                letters[ord(l)] -= 1

            res = max(res, right - left + 1)

            right += 1

        return res
