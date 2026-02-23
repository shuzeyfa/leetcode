class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1=version1.split(".")
        list2=version2.split(".")
        need=0
        for i in range(min(len(list1),len(list2))):
            if int(list1[i])>int(list2[i]):
                need=1
                break
            elif  int(list1[i])<int(list2[i]): 
                need=-1
                break
            else:
                continue
        if need==0:
            if len(list1)>len(list2):
                for j in range(len(list2),len(list1)):
                    if int(list1[j])>0:
                        need=1
                        break
            elif len(list2)>len(list1):
                for j in range(len(list1),len(list2)):
                    if int(list2[j])>0:
                        need=-1
                        break
                    
        return need
        