n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
res = 0
cnt = 0

for coin in coins:
     if k // coin == 0:
         continue
     cnt = k // coin
     res += cnt
     k %= coin

print(res)
