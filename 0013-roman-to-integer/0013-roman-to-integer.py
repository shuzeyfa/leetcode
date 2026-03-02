class Solution:
    def romanToInt(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            if s[i]=="M":
                if i==0:
                    count+=1000
                else:
                    if s[i-1]=="C":
                        count+=800
                    else:
                        count+=1000
            elif s[i]=="D":
                if i==0:
                    count+=500
                else:
                    if s[i-1]=="C":
                        count+=300
                    else:
                        count+=500  
            elif s[i]=="C":
                if i==0:
                    count+=100
                else:
                    if s[i-1]=="X":
                        count+=80
                    else:
                        count+=100
            elif s[i]=="L":
                if i==0:
                    count+=50
                else:
                    if s[i-1]=="X":
                        count+=30
                    else:
                        count+=50
            elif s[i]=="X":
                if i==0:
                    count+=10
                else:
                    if s[i-1]=="I":
                        count+=8
                    else:
                        count+=10
            elif s[i]=="V":
                if i==0:
                    count+=5
                else:
                    if s[i-1]=="I":
                        count+=3
                    else:
                        count+=5
            else:
                count+=1
        return count                