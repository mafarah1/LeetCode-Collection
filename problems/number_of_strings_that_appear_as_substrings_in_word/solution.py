class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        sol = 0
        
        for string in patterns:
            if string in word:
                sol += 1
        
        return sol
        