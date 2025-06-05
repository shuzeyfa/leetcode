from collections import defaultdict
import sys
import threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m, k = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    stack = []
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        stack.append(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, node)
            elif nei == parent:
                continue
            else:
                if nei in stack:
                    ind = stack.index(nei)
                    stack2 = stack[ind:]
                    if len(stack2) > k:
                        print(len(stack2))
                        print(*stack2)
                        exit()
        stack.pop()

    for i in range(1, n + 1):
        if i not in visited:
            dfs(i, -1)

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()