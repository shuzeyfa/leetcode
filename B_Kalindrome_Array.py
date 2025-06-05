def check(left2,right2,val,l2):
    while left2<right2:
        if l2[left2] == l2[right2]:
            right2 -= 1
            left2 += 1
        elif l2[left2] == val:
            left2 += 1
        elif l2[right2] == val:
            right2 -= 1
        else:
            return False
    return True



for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if n == 1:
        print("YES")
    else:
        left,right = 0, n-1
        t=False
        while left<right:
            if l[left] == l[right]:
                left += 1
                right -=1
            else:
                t=True
                break
        if t==False:
            print("YES")
        else:
            if check(left,right,l[left],l) or check(left,right,l[right],l):
                print("YES")
            else:
                print("NO")