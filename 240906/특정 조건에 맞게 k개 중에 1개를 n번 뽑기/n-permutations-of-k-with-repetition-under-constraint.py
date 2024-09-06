import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ans = []

def choose(num):
    if num == n+1:
        print(*ans)
        return

    for i in range(1, k+1):
        if num < 3:
            ans.append(i)
            choose(num+1)
            ans.pop()
        elif ans[-1] != i or ans[-2] != i:
            ans.append(i)
            choose(num+1)
            ans.pop()

choose(1)