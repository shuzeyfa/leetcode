def find(s,a):
    if len(s)==1 and s==a:
        return 0
    if len(s)==1:
        return 1
    
    s2 = s[:len(s)//2] 
    s3 = s[len(s)//2:]
    
    ind= ord(a)-ord("a")
    ind += 1
    ind = ind%26
    ind += ord("a")
    c = chr(ind)
    temp4 = s2.count(c)
    temp5 = s3.count(c)
    temp = s2.count(a) + temp5
    temp2 = s3.count(a) + temp4
    if temp>=temp2:
        ind= ord(a)-ord("a")
        ind += 1
        ind = ind%26
        ind += ord("a")
        c = chr(ind)
        return len(s2)-s2.count(a) + find(s3,c)
    else:
        ind= ord(a)-ord("a")
        ind += 1
        ind = ind%26
        ind += ord("a")
        c = chr(ind)
        return len(s3)-s3.count(a) + find(s2,c)
    
    

for _ in range(int(input())):
    n = int(input())
    s = input()
    a = "a"
    final = find(s,a)
    print(final)

