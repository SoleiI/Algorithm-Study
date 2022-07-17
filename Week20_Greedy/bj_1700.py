# 백준 1700) 멀티탭 스케줄링
# 입력 : 멀티탭 구멍의 개수 N, 전기용품의 총 사용 횟수 K, 전기용품의 이름(사용 순서)
# 출력 : 하나씩 플러그를 빼는 최소의 횟수

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
products = deque(list(map(int, sys.stdin.readline().split())))

multitap = [0] * n
count = 0
while products:
  product = products.popleft()

  if product in multitap:
    continue

  elif 0 in multitap:
    for j in range(n):
      if multitap[j] == 0:
        multitap[j] = product
        break

  else:
    idx = []
    for tap in multitap:
      if tap not in products:
        idx.append(1000)
      else:
        idx.append(products.index(tap))
    
    change = idx.index(max(idx))
    multitap[change] = product
    count += 1

print(count)