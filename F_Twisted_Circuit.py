a=int(input())
b=int(input())
c=int(input())
d=int(input())
first=a or b

second = 1 if c!=d else 0

third = c and b
fourth = a or d
fifth = first and second
six = 1 if third != fourth else 0

# print(fifth)
print(0 if (fifth or six) else 1)