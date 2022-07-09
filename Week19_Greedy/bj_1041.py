# 백준 1041) 주사위
# 입력 : N, 주사위에 쓰여 있는 수
# 출력 : N^3개의 주사위로 만든 N^3 크기의 정육면체에 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값

import sys
n = int(sys.stdin.readline())
dice = list(map(int,sys.stdin.readline().split()))

if n == 1:
  print(sum(dice) - max(dice))
else:
  a = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
  one_count = (n - 2) ** 2 + (n - 2) * (n - 1) * 4
  two_count = (n - 2) * 4 + (n - 1) * 4

  one = one_count * min(a)
  two = two_count * (sum(a) - max(a))
  three = 4 * sum(a)

  print(one + two + three)
