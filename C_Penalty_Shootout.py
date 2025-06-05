for _ in range(int(input())):
    s = input()
    a = b =a2= b2 =0
    a3=b3=5
    t=True
    for i in range(10):
        if i % 2==0:
            if s[i]=="1":
                a+=1
            elif s[i]=="?":
                a2+=1
            a3-=1
            temp = a+a2
            if temp - b > b3:
                print(i+1)
                t = False
                break

            temp = b+b2
            if temp - a>a3:
                print(i+1)
                t = False
                break

        else:
            if s[i]=="1":
                b += 1
            elif s[i]=="?":
                b2+=1
            b3-=1
            temp = b+b2
            if temp - a>a3:
                print(i+1)
                t = False
                break
            
            temp = a+a2
            if temp - b > b3:
                print(i+1)
                t = False
                break
    if t==True:
        print(10)