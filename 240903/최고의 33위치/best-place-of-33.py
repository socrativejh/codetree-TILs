import sys
input = sys.stdin.readline
n = int(input())
graph = []
max_num = 0

for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

def get_num_gold(row, col):
    num = 0
    for i in range(row, row+3):
        for j in range(col, col+3):
            num += graph[i][j]
    return num

for i in range(n):
    for j in range(n):
        if i + 2 >= n or j + 2 >= n:
            continue
        num = get_num_gold(i, j)

        max_num = max(max_num, num)

print(max_num)