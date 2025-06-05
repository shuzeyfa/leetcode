n = 3

temp = []
res= []

def back():
    if len(temp) == n*2:
        temp2 = "".join(temp)
        res.append(temp2)
        return 
    
    for i in range(2):
        if i == 0:
            temp.append("(")
        else:
            temp.append(")")
        back()

        temp.pop()
        
back()
l=[]

def check(s):
    stack = []
    for j in s:
        if j == "(":
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0
for i in res:
    if check(i):
        l.append(i)
print(l)

