class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total=0
        index1, index2 =0, len(skill)-1
        summ=skill[0]+skill[-1]
        while index1<index2:
            if (skill[index1]+skill[index2])!=summ:
                return -1
            else:
                total+=((skill[index1]*skill[index2]))
                index1+=1
                index2-=1
        return total