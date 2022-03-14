# 리트코드 112) Best Time to Buy and Sell Stock II
# 입력 : 주식의 가격으로 이루어진 배열
# 출력 : 최대 이익

prices = [7,6,4,3,1]    # 가격 배열
stock = 0               # 주식 개수
buyPrice = 0            # 구매 가격
profit = 0              # 이익

for i in range(len(prices)-1):
  if prices[i] < prices[i+1]:   # 다음에 오르는 경우
    if stock == 0:
      stock = 1
      buyPrice = prices[i]
  else:                         # 다음에 떨어지는 경우
    if stock == 1:
      stock = 0
      profit += prices[i] - buyPrice
      buyPrice = 0

if stock == 1:
  profit += prices[-1] - buyPrice

print(profit)