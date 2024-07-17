import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque(range(1, n+1))

while q:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    q.append(q.popleft())