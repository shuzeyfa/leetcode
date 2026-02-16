class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        l=[mat[0][0]]
        index1,index2=0,1
        down=True
        if len(mat[0])>1:
            for _ in range(len(mat)+len(mat[0])-3):
                if down==True:
                    while index2>0 and index1<len(mat)-1:
                        l.append(mat[index1][index2])
                        index1+=1
                        index2-=1
                    l.append(mat[index1][index2])
                    if index1<(len(mat)-1):
                        index1+=1
                    else:
                        index2+=1
                    down=False
                else:
                    while index1>0 and index2<len(mat[0])-1:
                        l.append(mat[index1][index2])
                        index1-=1
                        index2+=1
                    l.append(mat[index1][index2])
                    if index2<(len(mat[0])-1):
                        index2+=1
                    else:
                        index1+=1
                    down=True
            if len(mat)!=1 or len(mat[0])!=1:
                l.append(mat[len(mat)-1][len(mat[0])-1])
            return (l)
        else:
            for i in range(1,len(mat)):
                l.append(mat[i][0])
            return (l)