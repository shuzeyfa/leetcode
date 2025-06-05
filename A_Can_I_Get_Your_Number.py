n =  int(input())
l = []
for i in range(n):
    l.append(input())
count = 0
for i in range(len(l[0])):
    char = l[0][i]
    t=True
    for j in range(n):
        if l[j][i] != char:
            t=False
            break
    if t==False:
        break
    else:
        count += 1
print(count)


