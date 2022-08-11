# 백준 15686) 치킨 배달
# 입력 : 도시의 크기 N, 치킨집의 개수 M, 도시의 정보
# 출력 : 도시의 치킨 거리의 최솟값

import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

houses = []
chickens = []
for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      houses.append([i, j])
    elif city[i][j] == 2:
      chickens.append([i, j])

min_distance = 10000
for chicken in combinations(chickens, m):
  distance = 0
  for house in houses:
    min_diff = 100
    for chick in chicken:
      diff = abs(house[0] - chick[0]) + abs(house[1] - chick[1])
      min_diff = min(min_diff, diff)
    distance += min_diff
  
  min_distance = min(min_distance, distance)

print(min_distance)