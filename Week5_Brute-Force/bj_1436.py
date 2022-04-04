# 백준 1436) 영화감독 숌
# 입력 : E, S, M
# 출력 : E S M으로 표시되는 가장 빠른 연도

import sys
e, s, m = map(int, sys.stdin.readline().split())

for year in range(1, 7981):
  ee = year % 15 if year % 15 != 0 else 15
  ss = year % 28 if year % 28 != 0 else 28
  mm = year % 19 if year % 19 != 0 else 19
  if ee == e and ss == s and mm == m:
    break

print(year)