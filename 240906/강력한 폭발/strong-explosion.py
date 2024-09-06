import sys
input = sys.stdin.readline

graph = []
n = int(input())
for _ in range(n): graph.append(list(map(int, input().split())))
d1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
d3 = [(-2, 0), (-1, 0), (1, 0), (2, 0)]

bomb_loc = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]

# 폭탄의 폭발 방식 저장할 리스트
bomb = []

def cnt_bomb():
    loc = set()
    for i in range(len(bomb_loc)):
        x, y = bomb_loc[i]
        loc.add((x, y))
        if bomb[i] == 1:
            # 상하좌우 1칸 폭발
            for dx, dy in d1:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    loc.add((nx, ny))
        elif bomb[i] == 2:
            # 대각선 1칸 폭발
            for dx, dy in d2:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    loc.add((nx, ny))
        else:
            # 상하 2칸 폭발
            for dx, dy in d3:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    loc.add((nx, ny))
    return len(loc) # 폭발한 영역 개수

def is_most(now, most_bomb):
    if now == len(bomb_loc): # 폭발 방식 다 골랐으면 폭발하는 영역 개수 count -> max 구하기
        cnt = cnt_bomb() 
        return max(most_bomb, cnt)
    
    for i in range(1, 4): # 모든 폭발 경우의 수를 탐색 (완전탐색?)
        bomb.append(i)  # 폭탄의 폭발 방식 선택 (1, 2, 3 중 하나)
        most_bomb = is_most(now + 1, most_bomb) # 다음 폭탄으로 넘어가 -> 다시 폭탄 방식 선택 (재귀)
        bomb.pop() 
    
    return most_bomb


print(is_most(0, 0))