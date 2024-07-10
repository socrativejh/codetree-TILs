import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    key = arr[i]

    j = i-1
    while j >=0 and key < arr[j]:
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
        j = j-1

for i in arr:
    print(i, end=" ")