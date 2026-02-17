class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l=[[],[],[]]
        for i in range(9):
            if i%3==0:
                l=[[],[],[]]
            for j in range(9):
                if j<3:
                    if board[i][j]!="." and board[i][j] in l[0]:
                        return False
                    elif board[i][j]!=".":
                        l[0].append(board[i][j])
                elif j<6:
                    if board[i][j]!="." and board[i][j] in l[1]:
                        return False
                    elif board[i][j]!=".":
                        l[1].append(board[i][j])
                else:
                    if board[i][j]!="." and board[i][j] in l[2]:
                        return False
                    elif board[i][j]!=".":
                        l[2].append(board[i][j])

        for i in range(9):
            row=[]
            for j in range(9):
                if board[i][j]!="." and board[i][j] in row:
                    return False
                elif board[i][j]:
                    row.append(board[i][j])
        for i in range(9):
            col=[]
            for j in range(9):
                if board[j][i]!="." and board[j][i] in col:
                    return False
                elif board[j][i]!=".":
                    col.append(board[j][i])
        return True


       