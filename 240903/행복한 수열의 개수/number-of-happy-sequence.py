import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
seq1 = []; seq2 = []; num = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 끊어진 후 부분에서 더 길게 연속될 수 있음 (max_cnt 선언)
def happy(seq):
    cnt = 1
    max_cnt = 1
    for i in range(n-1):
        if seq[i] == seq[i+1]:
            cnt += 1
        else:
            if max_cnt < cnt: 
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt: max_cnt = cnt
    if max_cnt >= m:
        return True
    return False

for i in range(n):
    seq1 = []
    seq2 = []
    for j in range(n):
        if len(seq1) > n or len(seq2) > n: continue
        seq1.append(graph[i][j])
        seq2.append(graph[j][i])
    if happy(seq1): num += 1
    if happy(seq2): num += 1

print(num)