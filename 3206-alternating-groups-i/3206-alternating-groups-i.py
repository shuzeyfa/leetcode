class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count=0
        for i in range(len(colors)-2):
            if colors[i]==0:
                if colors[i+1]==1 and colors[i+2]==0:
                    count+=1
            else:
                if colors[i+1]==0 and colors[i+2]==1:
                    count+=1
        if colors[0]==0:
            if colors[len(colors)-2]==0 and colors[len(colors)-1]==1:
                count+=1
        else:
            if colors[len(colors)-2]==1 and colors[len(colors)-1]==0:
                count+=1
        if colors[len(colors)-1]==0:
            if colors[0]==1 and colors[1]==0:
                count+=1
        else:
            if colors[0]==0 and colors[1]==1:
                count+=1
        return count