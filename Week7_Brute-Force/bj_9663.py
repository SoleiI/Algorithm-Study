# 백준 9663) N-Queen
# 입력 : N
# 출력 : 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

def checkQueen(row, col):
  for queen in queens:
    if queen[1] == col or abs(row-queen[0]) == abs(col-queen[1]):
      return False
  return True
  
def findCases(i):
  global count
  for j in range(n):
    if len(queens) == 0 or checkQueen(i, j):
      queens.append([i, j])
      if i < n-1:
        findCases(i+1)
      if len(queens) == n:
        count += 1
      queens.pop()

if __name__ == '__main__':
  n = int(input())
  count = 0
  queens = []

  findCases(0)
  print(count)