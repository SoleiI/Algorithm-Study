# 백준 1003) 피보나치 함수
# 입력: 테스트 케이스 개수 T, n
# 출력: 0이 출력되는 횟수, 1이 출력되는 횟수

import sys
t = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for _ in range(t):
  n = int(sys.stdin.readline())
  if dp[n][0] == 0 and dp[n][1] == 0:
    for i in range(2, n+1):
      if dp[n][0] or dp[n][1]:
        continue
      dp[i][0] = dp[i-1][0] + dp[i-2][0]
      dp[i][1] = dp[i-1][1] + dp[i-2][1]
  print(dp[n][0], dp[n][1])