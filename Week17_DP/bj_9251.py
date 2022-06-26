# 백준 9251) LCS
# 입력 : 알파벳 대문자로만 이루어진 문자열 2개
# 출력 : 두 문자열의 LCS의 길이

a = '0' + input()
b = '0' + input()
dp = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
  for j in range(1, len(b)):
    if a[i] == b[j]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])