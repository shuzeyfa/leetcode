for _ in range(int(input())):
    n = int(input())
    s = input()
    ind = 0
    maxx = 0
    zero = 0
    one = 0
    for i in range(n):
        if s[i] == "0":
            zero += 1
        else:
            one += 1
    if zero == n:
        print(n)
    elif one == n:
        print(n+1)
    else:

        left=right =float("inf")
        while ind<n:
            char = s[ind]
            count = 1
            temp = ind
            ind += 1
            
            while ind<n and s[ind] == char:
                count += 1
                ind += 1
            if count > maxx:
                maxx = count
                left = temp
                right = ind 
        
        tot = 0
        ind2 = 0
        sign = int(s[0])
        
        while ind2<n:
            if ind2 == 0:
                if s[ind2] == "0":
                    tot += 1
                else:
                    if left == 0:
                        tot += 1
                    else:
                        tot += 2
                ind2 += 1
            elif s[ind2] == str(sign):
                tot += 1
                ind2 += 1
            else:
                if left == ind2:
                    tot += 1
                elif ind2 == right:
                    tot += 1
                else:
                    tot += 2
                sign = int(s[ind2])
                ind2 += 1
        print(tot)