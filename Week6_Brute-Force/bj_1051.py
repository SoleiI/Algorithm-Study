# 백준 1051) 숫자 정사각형
# 입력 : N, M, N*M 크기의 직사각형
# 출력 : 꼭짓점의 수가 모두 같은 가장 큰 정사각형의 크기

import sys
n, m = map(int, sys.stdin.readline().split())
square = list(sys.stdin.readline().strip() for _ in range(n))
maxSize = 1

def isSquare(x, y1, y2):
  length = y2 - y1
  xx = x + length
  if xx < n:
    if square[x][y1] == square[x][y2] == square[xx][y1] == square[xx][y2]:
      return (length + 1) ** 2
  return 1

for x in range(n):
  for y1 in range(m-1):
    num = square[x][y1]
    for y2 in range(y1+1, m):
      maxSize = max(maxSize, isSquare(x, y1, y2))

print(maxSize)