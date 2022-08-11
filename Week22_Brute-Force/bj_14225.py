# 백준 14225) 부분수열의 합
# 입력 : 수열의 크기 N, 수열 S
# 출력 : 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수

import sys
from itertools import combinations

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

sum_list = []
for i in range(1, n+1):
  for nums in combinations(s, i):
    sum_list.append(sum(nums))

sum_list = list(set(sorted(sum_list)))

for i in range(2000000):
  if i > len(sum_list) - 1:
    break
  elif sum_list[i] != i+1:
    break

print(i+1)