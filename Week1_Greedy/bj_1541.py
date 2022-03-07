# 백준 1541) 잃어버린 괄호
# 입력 : 5자리 이하 숫자, +, -으로 이루어진 식
# 출력 : 식의 값이 최소인 연산 결과

# 식
formula = input()   # 식
cal = braket = 0

arr = formula.split('-')

for i in arr[0].split('+'):
  cal += int(i)

for i in arr[1:]:
  braket = 0
  if '+' in i:
    for j in i.split('+'):
      braket += int(j)
  else:
    braket = int(i)
  
  if '-' in formula:
    cal -= braket
  else:
    cal += braket

print(cal)