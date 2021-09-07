class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ansKey = keysPressed[0]
        ansDuration = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > ansDuration or duration == ansDuration and key > ansKey:
                ansKey = key
                ansDuration = duration
        return ansKey
    
        #Ohhhhhhhhh, instead of saving all the values, just dethrone any value that has now the longest duration. and compare them lexographically