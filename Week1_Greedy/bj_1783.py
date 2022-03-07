# 백준 1783) 병든 나이트
# 입력 : 체스판의 세로 길이 N와 가로 길이 M
# 출력 : 병든 나이트가 방문할 수 있는 칸의 개수 최댓값

# 체스판
height, width = input().split()
height = int(height)
width = int(width)

# 방문한 칸 개수
count = 1

if height == 1:
  count = 1
elif height == 2:
  count += min(3, (width - 1) // 2)
else:
  if width < 7:
    count += min(3, width - 1)
  else:
    width -= 6
    count += 4 + (width - 1)

print(count)