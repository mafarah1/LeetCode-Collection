def setZeroesHelper(matrix,i,j):
    m = 0
    while j+m < len(matrix[i]):
        matrix[i][j+m] = 0
        m += 1
    m = 0
    while j - m > -1:
        matrix[i][j-m] = 0
        m += 1
    m = 0
    while i + m < len(matrix):
        matrix[i+m][j] = 0
        m += 1
    m = 0
    while i - m > -1:
        matrix[i-m][j] = 0
        m += 1

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroes.append([i,j])
        
        for pair in zeroes:
            setZeroesHelper(matrix,pair[0],pair[1])
        