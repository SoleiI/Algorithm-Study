# 백준 1715) 카드 정렬하기
# 입력 : 숫자 카드 묶음의 개수 N, 숫자 카드 묶음의 각각의 크기
# 출력 : 최소 비교 횟수

import sys, heapq
n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(cards)
count = 0

while len(cards) > 1:
  card1 = heapq.heappop(cards)
  card2 = heapq.heappop(cards)
  heapq.heappush(cards, card1 + card2)
  count += card1 + card2

print(count)