# 백준 4375) 1
# 입력 : 2와 5로 나누어 떨어지지 않는 정수 n 여러 개
# 출력 : 1로 이루어진 n의 배수 중 가장 작은 수의 자리수

while True:
  try:
    n = int(input())
    num = 1

    while num % n != 0:
      num = num * 10 + 1

    print(len(str(num)))

  except:
    break