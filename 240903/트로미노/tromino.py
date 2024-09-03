import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []; max_sum = 0
for i in range(n):
    graph.append(list(map(int, input().split())))

def find_1(x, y):
    max_sum = 0
    if x+1 < n and y+1 < m:
        sum_1 = graph[x][y] + graph[x][y+1] + graph[x+1][y]
    else: sum_1 = 0
    if x-1 >= 0 and y+1 < m:
        sum_2 = graph[x][y] + graph[x-1][y] + graph[x][y+1]
    else: sum_2 = 0
    if x-1 < n and y-1 >= 0:
        sum_3 = graph[x][y] + graph[x][y-1] + graph[x-1][y]
    else: sum_3 = 0
    if x+1 < n and y-1 >= 0:
        sum_4 = graph[x][y] + graph[x][y-1] + graph[x+1][y]
    else: sum_4 = 0
    max_sum = max(sum_1, sum_2, sum_3, sum_4)
    return max_sum

def find_2(x, y):
    max_sum = 0
    if x+2 < n:
        sum_1 = graph[x][y] + graph[x+1][y] + graph[x+2][y]
    else: sum_1 = 0
    if y+2 < m:
        sum_2 = graph[x][y] + graph[x][y+1] + graph[x][y+2]
    else: sum_2 = 0
    max_sum = max(sum_1, sum_2)
    return max_sum

for i in range(n):
    for j in range(m):
        max_sum = max(max_sum, find_1(i, j), find_2(i, j))

print(max_sum)