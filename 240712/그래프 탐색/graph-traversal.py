import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True

count = 0
for i in range(1, n+1):
    if graph[1][i]:
        count += 1

print(count)