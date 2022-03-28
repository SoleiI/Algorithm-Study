# 백준 1065) 한수
# 입력 : 1000 이하의 N
# 출력 : 1~N까지의 한수의 개수

n = int(input())
count = 0

def isSequence(num):
  avg = (num // 100 + num % 10) / 2
  tens = (num % 100) // 10
  if tens == avg:
    return True
  else:
    return False

if n < 100:
  count = n
else:
  count = 99
  huns = n // 100
  count += (huns-1)*5
  for i in range(huns*100, n+1):
    if isSequence(i):
      count += 1

print(count)