from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = input()
    zero = []
    one = []
    count = 0
    ans = []
    for i in s:
        if i == "0":
            if not one:
                count += 1
                ans.append(count)
                zero.append(count)
            else:
                k = one.pop()
                zero.append(k)
                ans.append(k)
        else:
            if not zero:
                count += 1
                ans.append(count)
                one.append(count)
            else:
                k = zero.pop()
                one.append(k)
                ans.append(k)
    print(count)
    print(*ans)