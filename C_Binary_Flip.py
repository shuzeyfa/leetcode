def check(a,b,zero,one,n):
    convert = False
    for i in range(n-1,-1,-1):
        char = a[i]
        if convert == True:
            if char == "0":
                char = "1"
            else:
                char = "0"
        
        if char == b[i]:
            if a[i] == "0":
                zero -= 1
            else:
                one -= 1
        else:
            if zero == one:
                if a[i] == "0":
                    zero -= 1
                else:
                    one -= 1
                if convert == False:
                    convert = True
                else:
                    convert = False
            else:
                return False

        
    return True

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    zero = one = 0
    for i in a:
        if i == "0":
            zero += 1
        else:
            one += 1
    
    if check(a,b,zero,one,n):
        print("YES")
    else:
        print("NO")