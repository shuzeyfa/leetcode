s="abcbadbrfxty"

s2 = set()
left, right = 0,0
count = 0
while right<len(s):
    if s[right] not in s2:
        s2.add(s[right])
        count = max(count, right - left+1)
        right += 1
    else:
        while s[right] in s2:
            s2.remove(s[left])
            left += 1
        count = max(count, right - left+1)
        s2.add(s[right])
        right += 1
print(count)
