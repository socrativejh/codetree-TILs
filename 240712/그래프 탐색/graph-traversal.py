import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
def dfs(v):
    global count
    for curr_v in graph[v]:
        if not visited[curr_v]:
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True
dfs(1)
print(count)