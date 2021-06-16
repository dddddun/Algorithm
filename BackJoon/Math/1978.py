def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for num in arr:
    if isPrime(num):
        cnt += 1
print(cnt)

