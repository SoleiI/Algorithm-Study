# 백준 16953) A -> B
# 입력 : 정수 A와 연산 결과 B
# 출력 : A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값 또는 -1

a, b = map(int, input().split())
count = 1   # 연산의 최솟값

while a != int(b):
  if a > b:
    count = -1
    break
  elif b % 2 == 0:          # b가 2로 나눠지는 경우
    b /= 2
    count += 1
  elif b % 10 == 1:         # b가 1로 끝나는 경우
    b //= 10
    count += 1
  else:
    count = -1
    break

print(count)