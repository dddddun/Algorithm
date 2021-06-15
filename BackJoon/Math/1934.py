T = int(input())

# 최대공약수
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# 최소공배수
def lcm(a, b):
    return a * b // mcd(a, b)


for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))