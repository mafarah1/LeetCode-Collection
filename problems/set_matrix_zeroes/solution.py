class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #You have to find the positions. Then do the function on each position from a List
                
        #Find positions
        zeroList = []
        zeroPosition = []
    
        # l stands for list. n stands for number
        for l in matrix:
            for n in l:
                if n == 0:
                    zeroList.append(matrix.index(l))
                    zeroPosition.append(l.index(n))
                    l[l.index(n)] = None

        print(zeroList)
        print(zeroPosition)
        
        for position in zeroList:
            for num in range(len(matrix[position])):
                matrix[position][num] = 0;
        
        for collumn in zeroPosition:
            for row in range(len(matrix)):
                matrix[row][collumn] = 0
        