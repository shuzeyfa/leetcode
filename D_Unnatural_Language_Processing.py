for _ in range(int(input())):
    n = int(input())
    s = input()
    i = n - 1
    ans = []
    v = set()
    v.update(("a","e"))
    c = set(("b","c","d"))
    while i > 0:
        if s[i] in v:
            ans.append(s[i-1:i+1])
            i -= 2
        else:
            ans.append(s[i-2:i+1])
            i -= 3
    ans.reverse()
    print(".".join(ans))