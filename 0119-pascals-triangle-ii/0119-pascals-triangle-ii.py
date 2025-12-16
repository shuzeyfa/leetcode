class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        pre = self.getRow(rowIndex - 1)

        cr = [1]
        for i in range(len(pre)-1):
            cr.append(pre[i] + pre[i+1])
        cr.append(1)

        return cr