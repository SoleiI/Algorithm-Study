# 백준 14501) 퇴사
# 입력 : N, 기간, 금액
# 출력 : 최대 이익

import sys
n = int(input())
counsel = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

maxProfit = 0

def findMaxProfit(day, profit):
  if day > n:
    return 0
  elif day == n:
    return profit
  else:
    p1 = findMaxProfit(day+counsel[day][0], profit+counsel[day][1])
    p2 = findMaxProfit(day + 1, profit)
    profit = max(profit, p1, p2)
    return profit

maxProfit = findMaxProfit(0, 0)

print(maxProfit)