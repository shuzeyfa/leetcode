


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def check(n,k):
        if n == k:
            return True
        elif k>n:
            return False
        elif n%3 != 0: 
            return False
        else:
            temp = n // 3
            temp2 = temp * 2
            return check(temp,k) or check(temp2,k)



    for _ in range(int(input())):
        n, k =map(int,input().split())
        if check(n,k):
            print("YES")
        else:
            print("NO")
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
