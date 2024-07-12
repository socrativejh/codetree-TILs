import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [] * (n)
visited = [[False] * (n) for _ in range(m)]

dx = [1, 0]
dy = [0, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))

def cango(x, y):
    if x < 0 or x >= m or y < 0 or y >= n: return False
    if not graph[x][y] or visited[x][y]: return False
    return True
 
def dfs(x, y):
    global flag
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if cango(nx, ny):
            if nx == m-1 and ny == n-1: 
                flag = 1
            visited[nx][ny] = True
            dfs(nx, ny)

flag = 0
visited[0][0] = True
dfs(0, 0)
print(flag)