# 백준 2503) 숫자 야구
# 입력 : 질문과 결과
# 출력 : 가능성이 있는 숫자 개수

import sys
n = int(input())
qna = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

count = 0

def isRightAnswer(x, question):
  s, b = 0, 0  # strike, ball
  q = str(question[0])

  for i in range(3):
    if x[i] == q[i]:
      s += 1
    elif x[i] in q:
      b += 1

  if s == question[1] and b == question[2]:
    return True
  else: return False

for i in range(123, 988):
  point = 0
  num = str(i)
  if '0' in num :
    continue
  elif len(set(num)) != len(num):
    continue
  else:
    for j in range(n):
      if isRightAnswer(num, qna[j]):
        point += 1
    if point == n:
      count += 1

print(count)