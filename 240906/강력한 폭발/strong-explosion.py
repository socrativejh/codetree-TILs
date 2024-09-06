import sys
input = sys.stdin.readline

graph = []
n = int(input())
for _ in range(n): graph.append(list(map(int, input().split())))
d1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
d3 = [(-2, 0), (-1, 0), (1, 0), (2, 0)]

def explode(x, y):
    cnt1 = 1; cnt2 = 1; cnt3 = 1
    for i in d1:
        nx = i[0] + x; ny = i[1] + y
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                cnt1 += 1
    for i in d2:
        nx = i[0] + x; ny = i[1] + y
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                cnt2 += 1
    for i in d3:
        nx = i[0] + x; ny = i[1] + y
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                cnt3 += 1

    max_ = max(cnt1, cnt2, cnt3)
    if max_ == cnt1:
        for i in d1:
            nx = i[0] + x; ny = i[1] + y
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 2
    elif max_ == cnt2:
        for i in d2:
            nx = i[0] + x; ny = i[1] + y
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 2
    else:
        for i in d3:
            nx = i[0] + x; ny = i[1] + y
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 2
    return max_

total = 0
num = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 2
            num = explode(i, j)
            total += num

print(total)