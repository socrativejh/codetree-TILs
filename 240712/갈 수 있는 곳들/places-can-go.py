import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
starts = []
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * (n) for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(m):
    starts.append(list(map(int, input().split())))

def cango(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] or visited[x][y]:
        return False
    return True

def bfs(a, b):
    global count
    visited[a][b] = True
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if cango(nx, ny):
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))
count = 1
for start in starts:
    bfs(start[0]-1, start[1]-1)

print(count)