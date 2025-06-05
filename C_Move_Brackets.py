for _ in range(int(input())):
    n = int(input())
    s = input()
    stack = []
    count = 0
    for i in s:
        if i == ")":
            if stack:
                stack.pop()
            else:
                count += 1
        else:
            stack.append(i)
    print(count)