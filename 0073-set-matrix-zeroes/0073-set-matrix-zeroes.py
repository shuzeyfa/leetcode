class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        val=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    val.append([i,j])
        for i,j in val:
            l=0
            while l<len(matrix[0]):
                matrix[i][l]=0
                l+=1
            l=0
            while l<len(matrix):
                matrix[l][j]=0
                l+=1
        