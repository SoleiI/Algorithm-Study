# 백준 11047) 동전 0
# 입력 : 첫째 줄에 N과 K, 둘째 줄부터 N개의 줄에 동전의 가치 오름차순으로
# 출력 : K원을 만드는데 필요한 동전 개수의 최솟값

# 동전 종류, 가격
coinType, price = input().split()
coinType = int(coinType)
price = int(price)

# 가격별 동전 -> 리스트에 저장
coins = []
for i in range(coinType):
  coin = int(input())
  coins.append(coin)

# 주어진 가격보다 작은 동전 중 가장 큰 단위의 동전부터 채우기
count = 0
for i in range(len(coins)-1, -1, -1):
  if price == 0 : break
  if coins[i] <= price :
    count += price // coins[i]
    price %= coins[i]
  
print(count)
