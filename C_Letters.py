l= [1,2,3,4,5,6,7]
k = 3
k = k%len(l)
l.reverse()
print(l)
l[k:] = reversed(l[k:])
l[:k] = reversed(l[:k])
print(l)