import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ans = set()

def choose(num):
    if num == n+1:
        for i in ans: print(i)
        return

    for i in range(1, k+1):
        ans.add(i)
        choose(num+1)
        ans.pop()

choose(1)