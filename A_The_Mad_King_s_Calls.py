for _ in range(int(input())):
    n = input()
    dig = n[0]
    final = 10*(int(dig)-1)
    for i in range(1,len(n)+1):
        final += i
    print(final)