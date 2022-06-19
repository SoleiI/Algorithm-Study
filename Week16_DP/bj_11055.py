# 백준 11055) 가장 큰 증가 부분 수열
# 입력 : 수열의 크기 N, 수열 A의 원소
# 출력 : 수열 A의 합이 가장 큰 증가 부분 수열의 합

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

for i in range(n):
  maxSum = 0
  index = i
  for j in range(i):
    if a[j] >= a[i]:
      continue
    if dp[j] > dp[index]:
      index = j
  dp[i] = a[i] + dp[index]

print(max(dp))