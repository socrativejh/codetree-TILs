import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[False] * (m) for _ in range(n)]
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))

def cango(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if not graph[x][y] or visited[x][y]: # 여기 or인거 잊지마
        return False
    return True

def bfs(a, b):
    global flag
    visited[a][b] = True
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if cango(nx, ny):
                if nx == n-1 and ny == m-1: 
                    flag = 1
                visited[nx][ny] = True
                q.append((nx, ny))

flag = 0
bfs(0, 0)
print(flag)