for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    if n == 0:
        print(0)
        continue

    val3 = 0
    for num in l:
        val3 |= num

    val4 = l[0]
    for num in l[1:]:
        val4 &= num

    print(val3 - val4)
