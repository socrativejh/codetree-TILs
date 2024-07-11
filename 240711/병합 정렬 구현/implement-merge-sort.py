import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def merge(arr, low, high):
    tmp = []
    mid = (low + high) // 2
    i = low; j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    while j <= high:
        tmp.append(arr[j])
        j += 1
    
    # 정렬된 결과 원본 배열에 넣어야지 원본 배열이 정렬됨
    for k in range(low, high+1):
        arr[k] = tmp[k-low]
    
    return arr


def merge_sort(arr, low, high):
    if (low >= high): return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    
    sorted_arr = merge(arr, low, high)

    return sorted_arr

print(*merge_sort(arr, 0, n-1))