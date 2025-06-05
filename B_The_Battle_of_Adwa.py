for i in range(int(input())):
    s = input()
    if len(s)<=10:
        print(s)
    else:
        temp= len(s)-2
        print(s[0]+str(temp)+s[-1])
