# 백준 10971) 외판원 순회 2
# 입력 : 도시의 수 N, 비용 행렬
# 출력 : 외판원의 순회에 필요한 최소 비용

import sys
from itertools import permutations

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_cost = 10000000
for i in permutations(range(n)):
  cities = list(i)
  cities.append(i[0])

  cost = 0
  for j in range(len(cities)-1):
    if w[cities[j]][cities[j+1]] == 0:
      cost = 10000001
      break

    else:
      cost += w[cities[j]][cities[j+1]]
  
  min_cost = cost if cost < min_cost else min_cost

print(min_cost)