# 백준 1912) 연속합
# 입력 : 정수 n, n개로 이루어진 수열
# 출력 : 가장 큰 연속합

import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
  dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))