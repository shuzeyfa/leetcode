for _ in range(int(input())):
    s = input()
    ind = float("inf")
    for i in range(len(s)):
        if s[i] == "0":
            ind = i+1
            break
    if ind == float("inf"):
        print(1,1,1,len(s))
    else:
        ind2 = ind
        s2 = ["1"]
        while ind2<len(s):
            if s[ind2] == "1":
                s2.append("0")
            else:
                s2.append("1")
            ind2 += 1
        temp = "".join(s2)
        if temp in s:
            print(ind-1,ind+len(temp)-2,1,len(s))
        else:
            print(1,len(s)-ind+1,1,len(s))
        