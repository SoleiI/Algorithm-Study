# 백준 10026) 적록색약
# 입력 : N, N*N 크기의 그림
# 출력 : 적록색약이 아닌 사람이 봤을 때의 구역의 수, 적록색약인 사람이 봤을 때의 구역의 수

import sys
sys.setrecursionlimit(10**7)
n = int(input())
picture = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visitN = [[False] * n for _ in range(n)]
visitRG = [[False] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def recursive_dfsN(i, j):
  global areaN
  visitN[i][j] = True
  for c in range(4):
    x = i + dx[c]
    y = j + dy[c]
    if x >= 0 and x < n and y >= 0 and y < n:
      if not visitN[x][y] and picture[i][j] == picture[x][y]:
        areaN += 1
        recursive_dfsN(x, y)

def recursive_dfsRG(i, j):
  global areaRG
  visitRG[i][j] = True
  for c in range(4):
    x = i + dx[c]
    y = j + dy[c]
    if x >= 0 and x < n and y >= 0 and y < n:
      if not visitRG[x][y]:
        if picture[i][j] != picture[x][y] and (picture[i][j] == 'B' or picture[x][y] == 'B'):
          continue
        areaRG += 1
        recursive_dfsRG(x, y)

countRG = 0
countN = 0

for i in range(n):
  for j in range(n):
    if not visitN[i][j]:
      areaN = 1
      recursive_dfsN(i, j)
      if areaN > 0:
        countN += 1
    if not visitRG[i][j]:
      areaRG = 1
      recursive_dfsRG(i, j)
      if areaRG > 0:
        countRG += 1

print(countN, countRG)