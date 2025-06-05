MOD = 10**9 + 7

def solve_bitwise_sum(arr):
    n = len(arr)
    result = 0

    for j in range(n):
        and_sum = 0
        or_sum = 0

        for i in range(n):
            and_sum = (and_sum + (arr[i] & arr[j])) % MOD

        for k in range(n):
            or_sum = (or_sum + (arr[j] | arr[k])) % MOD

        result = (result + and_sum * or_sum) % MOD

    return result
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(solve_bitwise_sum(l))