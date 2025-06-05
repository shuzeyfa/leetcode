n = int(input())
s=input()
stack = []
for i in range(n):
    if not stack:
        stack.append(s[i])
    else:
        if stack[-1] != s[i]:
            stack.pop()
        else:
            stack.append(s[i])
print(len(stack))