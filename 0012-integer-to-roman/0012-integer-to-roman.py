class Solution:
    def intToRoman(self, num: int) -> str:
        s=""
        while num>0:
            if num>=1000:
                rep=num//1000
                s+=("M"*rep)
                num=num%1000
            elif num>=500:
                if num>=900:
                    s+="CM"
                    num=num%900
                else:
                    rep=num//500
                    s+=("D"*rep)
                    num=num%500
            elif num>=100:
                if num>=400:
                    s+="CD"
                    num=num%400
                else:
                    rep=num//100
                    s+=("C"*rep)
                    num=num%100
            elif num>=50:
                if num>=90:
                    s+="XC"
                    num=num%90
                else:
                    rep=num//50
                    s+=("L"*rep)
                    num=num%50
            elif num>=10:
                if num>=40:
                    s+="XL"
                    num=num%40
                else:
                    rep=num//10
                    s+=("X"*rep)
                    num=num%10
            elif num>=5:
                if num>=9:
                    s+="IX"
                    num=num%9
                else:
                    rep=num//5
                    s+=("V"*rep)
                    num=num%5
            else:
                if num==4:
                    s+=("IV")
                    num=num%4
                else:
                    s+=("I"*num)
                    num=0
        return (s)