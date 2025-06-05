def check(s2):
    stack = []
    for i in s2:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0
for _ in range(int(input())):
    s = input()
    first = float("inf")
    for i in range(len(s)):
        if s[i] == "(":
            first = i
            break
    sec = float("inf")
    for i in range(len(s)-1,-1,-1):
        if s[i] == ")":
            sec= i
            break

    val = s[:first] + s[first+1:sec] + s[sec+1:]
    if not check(val):
        print("YES")
    else:
        print("NO")
