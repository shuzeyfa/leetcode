# Ramadan session

from math import log2, ceil

def solution():
    s = input()
    q = int(input())
    k = list(map(int, input().split()))
    ans = []
    def findChar(level, pos, invert):
        if level == 0:
            pos -= 1
            if invert:
                if s[pos].islower():
                    return s[pos].upper()
                else:
                    return s[pos].lower()
            else:
                return s[pos]
        
        number_of_chars = len(s) * (2**(level))
        mid = number_of_chars//2
        if pos > mid:
            return findChar(level-1, pos-mid, not invert)
        else:
            return findChar(level-1, pos, invert)
    
    for i in range(q):
        current_level = ceil(log2(k[i]/len(s) + 1))
        ans.append(findChar(current_level, k[i], False))

    return ans
        

t = int(input())
for _ in range(t):
    print(*solution())