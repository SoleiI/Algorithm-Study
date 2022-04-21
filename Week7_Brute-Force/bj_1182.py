# 백준 1182) 부분수열의 합
# 입력 : 정수의 개수 N, 정수 S
# 출력 : 합이 S가 되는 부분수열의 개수

def makeSequence(x, y, temp, amount):
  global count    # global 선언
  for i in range(x, y):
    temp.append(sequence[i])
    if len(temp) == amount:
      if sum(temp) == s:
        count += 1
    if y < n:
      makeSequence(i+1, y+1, temp, amount)
    temp.pop()

if __name__ == '__main__':
  n, s = map(int, input().split())
  sequence = list(map(int, input().split()))

  arr = []
  temp = []

  count = 0
  for i in range(1, n+1):
    makeSequence(0, n-i+1, temp, i)
  print(count)