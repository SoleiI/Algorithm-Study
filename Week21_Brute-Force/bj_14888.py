# 백준 14888) 연산자 끼워넣기
# 입력 : 수의 개수 N, A1 ~ AN, +, -, ×, ÷의 개수
# 출력 : 만들 수 있는 식의 최댓값과 최솟값

import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

op = ['+', '-', '*', '/']
operators = []
for i in range(4):
  for j in range(b[i]):
    operators.append(op[i])

def calculate(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  else:
    return int(num1 / num2)

max_num = -10**9
min_num = 10**9
for oper in permutations(operators):
  num1 = a[0]
  for i in range(1, n):
    num1 = calculate(num1, a[i], oper[i-1])
  max_num = num1 if max_num < num1 else max_num
  min_num = num1 if min_num > num1 else min_num

print(max_num)
print(min_num)