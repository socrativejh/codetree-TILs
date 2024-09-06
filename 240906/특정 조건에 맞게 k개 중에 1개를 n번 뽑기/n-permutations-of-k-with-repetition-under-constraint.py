import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ans = []

def choose(num):
    if num == n+1:
        for i in ans: print(i, end=" ")
        return

    for i in range(1, k+1):
        if num < 3:
            ans.append(i)
            choose(num+1)
            ans.pop()
        else:
            if ans[-1] != i and ans[-2] != i:
                ans.append(i)
                choose(num+1)
                ans.pop()

choose(1)