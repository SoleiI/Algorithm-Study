# 백준 1107) 리모컨
# 입력 : 채널 N, 고장난 버튼의 개수 M, 고장난 버튼
# 출력 : 채널 N으로 이동하기 위해 버튼을 누르는 최소 횟수

import sys
from itertools import product

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if n == 100:
  print(0)
  exit(0)

num = str(n)
if m == 0:
  print(min(len(num), abs(n - 100)))
  exit(0)

if m == 10:
  print(abs(n - 100))
  exit(0)

broken_btn = list(sys.stdin.readline().split())

button = []
for i in range(10):
  if not str(i) in broken_btn:
    button.append(str(i))

def isPossible(num):
  for i in str(num):
    if i in broken_btn:
      return False
  return True

if isPossible(n):
  print(min(len(num), abs(n - 100)))
  exit(0)

min_diff = 500000
for nums in product(button, repeat=len(num)):
  near_num = int(''.join(nums))
  if len(nums) != len(num):
    continue
  if abs(n - near_num) < min_diff:
    min_diff = abs(n - near_num)
num1 = len(num) + min_diff

num2 = 500000
if '1' in button:
  if '0' in button:
    near_num = int('1'+'0'*len(num))
  else:
    near_num = int('1'*(len(num)+1))
  num2 = len(num) + 1 + abs(n - near_num)

num3 = 500000
if len(num) > 1:
  near_num = int(button[-1]*(len(num)-1))
  num3 = len(num) - 1 + abs(n - near_num)

print(min(num1, num2, num3, abs(n - 100)))