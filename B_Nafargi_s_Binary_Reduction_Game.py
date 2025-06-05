n = int(input())
s = input()
stack=[]
for i in s:
    if len(stack) == 0:
        stack.append(i)
    else:
        if i == "0":
            if stack[-1] == "1":
                stack.pop()
            else:
                stack.append(i)
        else:
            if stack[-1] == "0":
                stack.pop()
            else:
                stack.append(i)

print(len(stack))