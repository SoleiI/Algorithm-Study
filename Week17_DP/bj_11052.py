# 백준 11052) 카드 구매하기
# 입력 : 카드의 개수 N, 카드팩 별 금액
# 출력 : 카드 N개를 갖기 위해 지불해야 하는 최대 금액

import sys
n = int(sys.stdin.readline())
cardpacks = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)

for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = max(dp[i], dp[i-j] + cardpacks[j])

print(dp[n])