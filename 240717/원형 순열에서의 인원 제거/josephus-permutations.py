import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()

q = deque(range(1, n+1))

while q:
    for i in range(k-1):
        q.append(q.popleft())
    print(q.popleft(), end=' ')