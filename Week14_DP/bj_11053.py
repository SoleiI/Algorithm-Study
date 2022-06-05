# 백준 11053) 가장 긴 증가하는 부분 수열
# 입력: 수열 A의 크기 N, 수열
# 출력: 수열 A의 가장 긴 증가하는 부분 수열의 길이

import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = 1

for i in range(1, n):
  temp = min(a[:i])
  if a[i] <= temp:
    dp[i] = 1
    index = i
    continue
  else:
    minIndex = a.index(temp)
    index = minIndex
    for j in range(i):
      if a[j] < a[i] and dp[index] <= dp[j]:
        index = j

  if a[i] > a[index]:
    dp[i] = dp[index] + 1
  elif a[i] == a[index]:
    dp[i] = dp[index]

print(max(dp))
