def one_letter(start: int, destination: int) -> int:
    alphabet = 26 # Total number of letters in the alphabet
    
    path = 0
    
    # Counterclockwise
    cc = 0
    for num in range(1,alphabet+1):
        if num < min(start,destination) or num >= max(start,destination):
            cc += 1

    path = min(cc, abs(destination-start)) 
    # The shortest distance from the initial "start" letter to the "destination" letter
    print()
    print(path)
    path += 1 # I must add one to take the choosing of the letter into account
    print(path)
    print(start, destination)
    
    return path

class Solution:
    def minTimeToType(self, word: str) -> int:
        solution = 0
        solution += one_letter(ord("a")-ord("a")+1,ord(word[0])-ord("a")+1)
        for i in range(len(word)-1):
            #print(solution)
            solution += one_letter(ord(word[i])-ord("a")+1,ord(word[i+1])-ord("a")+1)
            print(solution)
        
        return solution