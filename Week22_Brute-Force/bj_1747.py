# 백준 1747) 소수&팰린드롬
# 입력 : N
# 출력 : N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서 가장 작은 수

n = int(input())

if n == 1:
  print(2)
else:
  for i in range(n, 1004000):
    isPalin = False
    num = str(i)
    if num == num[::-1]:      # 팰린드롬 판별
      isPalin = True
    
    isPrime = True
    if isPalin == True:
      for j in range(2, n):   # 소수 판별
        if i % j == 0:
          isPrime = False
          break
    
    if isPrime and isPalin == True:
      print(i)
      break