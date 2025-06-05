l = []
s = input()
for i in range(1,len(s)//2 + 1):
    if s[:i] == s[len(s)-i:]:
        l.append(i)
print(len(l)+1)
for i in range(len(l)):
    val = s.count(s[:l[i]])
    print(l[i],val)
if s[:len(s)//2] == s[len(l)//2:]:
    print(len(l)//2,2)
print(len(s),1)
