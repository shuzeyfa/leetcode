n=int(input())
s=input()
count=0
left=0
ans = 0
for right in range(len(s)):
    if s[right]=="1":
        count += 1
    while count>n:
        if s[left]=="1":
            count -= 1
        left+=1
    ans += right - left +1
print(ans)