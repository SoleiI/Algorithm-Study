# 백준 2156) 포도주 시식
# 입력 : 포도주 잔의 개수 n, 포도주의 양
# 출력 : 최대로 마실 수 있는 포도주의 양

import sys
n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * n
dp[0] = wine[0]

for i in range(1, n):
  if i == 1:
    dp[i] = wine[i] + dp[0]
  elif i == 2:
    dp[i] = wine[i] + max(wine[0], wine[1])
  elif i == 3:
    dp[i] = wine[i] + max(wine[0] + wine[2], wine[0] + wine[1])
  else:
    dp[i] = wine[i] + max(wine[i-1] + dp[i-3], wine[i-1] + dp[i-4], dp[i-2])

print(max(dp))