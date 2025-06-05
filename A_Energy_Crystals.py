for _ in range(int(input())):
    n = int(input())
    count = 0
    while n > 1:
        count += 2
        n //= 2
    count += 3
        
    print(count)