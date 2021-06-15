'''
def gcd(x, y):
    a = y
    b = x % y

    # 이렇게 하면 변수를 따로 쓰지 않아도 된다.
    # x = x % y
    # x, y = y, x

    return a, b


def lcm(x, y, gcd):
    return x * y // gcd


A, B = map(int, input().split())
a = A
b = B
while b != 0:
    a, b = gcd(a, b)

print(a)
print(lcm(A, B, a))
'''




# 내가 하려고 했던 방법

a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
