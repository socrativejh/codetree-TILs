import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1):
    min_ = i
    for j in range(i+1, n):
        if arr[j] < arr[min_]:
            min_ = j
    tmp = arr[i]
    arr[i] = arr[min_]
    arr[min_] = tmp

print(*arr)