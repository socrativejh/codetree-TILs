import sys
input = sys.stdin.readline

n, t = map(int, input().split())
graph = []
graph.append(list(map(int, input().split())))
graph.append(list(map(int, input().split())))

def move():
    temp1 = graph[0][n-1]
    temp2 = graph[1][n-1]
    for i in range(2):
        for j in range(n-1, 0, -1):
            graph[i][j] = graph[i][j-1]

    graph[1][0] = temp1
    graph[0][0] = temp2

for i in range(t):
    move()

for i in range(2):
    print(*graph[i])