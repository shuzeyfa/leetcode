import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

input = lambda: sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        visited = [[False] * k for _ in range(n)]
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        

if __name__ == '__main__':
    threading.Thread(target=main).start()
