def check(char):
    left, right = 0, n-1
    count = 0
    while left<right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if s[left] == char:
                count += 1
                left += 1
            elif s[right] == char:
                count+= 1
                right-=1
            else:
                return float("inf")
    return count

for _ in range(int(input())):
    n = int(input())
    s = input()
    left, right = 0 , n-1
    t=True
    while left<right:
        if s[left]!=s[right]:
            t=False
            break
        left+=1
        right-=1
    if t:
        print(0)
    else:
        first = check(s[left])
        second = check(s[right])
        ans = min(first,second)
        print(ans if ans != float("inf") else -1)