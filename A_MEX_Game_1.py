costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

dif = []
for i,j in costs:
    dif.append(i-j)

d={}

for i,val in enumerate(dif):
    d[i]=val

so = dict(sorted(d.items(), key=lambda item:item[1]))
tot = 0
n = len(costs)//2
for i in so:
    if n>0:
        tot += costs[i][0]
        n -= 1
    else:
        tot += costs[i][1]

print(tot)