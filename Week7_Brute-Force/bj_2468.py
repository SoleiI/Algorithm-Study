# 백준 2468) 안전 영역
# 입력 : N, N*N만큼의 높이 정보
# 출력 : 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수

import sys
sys.setrecursionlimit(10**7)
n = int(input())
area = []
for i in range(n):
  area.append(list(map(int, sys.stdin.readline().split())))

maxArea = 1                     # 안전 영역의 최대 개수
maxHeight = 0                   # 지역에 있는 최대 높이

for i in range(n):
  for j in range(n):
      maxHeight = max(maxHeight, area[i][j])

def checkAdjacent(i, j, height):
  safeArea[i][j] = True
  if j+1 < n and safeArea[i][j+1] == False and area[i][j+1] > height:
    checkAdjacent(i, j+1, height)   # 오른쪽

  if i+1 < n and safeArea[i+1][j] == False and area[i+1][j] > height:
    checkAdjacent(i+1, j, height)   # 위쪽
  
  if j > 0 and safeArea[i][j-1] == False and area[i][j-1] > height:
    checkAdjacent(i, j-1, height)   # 왼쪽
  
  if i > 0 and safeArea[i-1][j] == False and area[i-1][j] > height:
    checkAdjacent(i-1, j, height)   # 아래쪽

def countSafeArea(height):
  count = 0
  for i in range(n):
    for j in range(n):
      if safeArea[i][j] == False and area[i][j] > height:
        checkAdjacent(i, j, height)
        count += 1
  return count

for i in range(1, maxHeight+1):
  safeArea = [[False] * n for _ in range(n)]   # 안전 영역에 포함되었는지 여부 체크
  maxArea = max(maxArea, countSafeArea(i))

print(maxArea)