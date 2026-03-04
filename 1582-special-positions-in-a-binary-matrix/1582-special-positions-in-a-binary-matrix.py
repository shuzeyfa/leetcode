class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        ans = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count = 0
                    for k in range(len(mat)):
                        if mat[k][j] == 1:
                            count += 1
                    for k in range(len(mat[0])):
                        if mat[i][k] == 1:
                            count += 1
                    if count == 2:
                        ans += 1
        return ans