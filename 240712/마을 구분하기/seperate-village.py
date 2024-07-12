import sys
input = sys.stdin.readline
graph = []

n = int(input())
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * (n) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def cango(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return False
    if not graph[x][y] or visited[x][y]: return False
    return True

def dfs(x, y):
    global human_count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if cango(nx, ny):
            visited[nx][ny] = True
            human_count += 1
            dfs(nx, ny)

# 상하좌우 다 막혀도 더 알아봐야함 -> 모든 좌표에 대해서 dfs 시작해보기 (if문 있지만)
vilages = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True # 맨처음 돌리는건 dfs 전에 True로 해줘야 (각 섬에서) 중복이 안됨 (사람수가 +1 씩 더 나옴)
            human_count = 1
            dfs(i, j)
            vilages.append(human_count)

vilages.sort()
print(len(vilages))
for v in vilages:
    print(v)