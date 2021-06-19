# 소수판별 (에라토스테네스 체)
def prime_list(n):
    prime = [True for _ in range(n + 1)]
    for i in range(2, int(n ** 0.5 + 1)):
        if prime[i]:
            for j in range(i + i, n + 1, i):
                prime[j] = False
    return prime

# 골드바흐의 추측
def goldbach(prime):
    for i in range(3, n // 2 + 1):
        if prime[i] and prime[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")


if __name__ == "__main__":
    prime = prime_list(1000000)
    while True:
        n = int(input())
        if n == 0: break
        goldbach(prime)




'''
def combination_with_replacement(L, s, sum):
    # 굳이 이렇게 풀어야 겠다면, 리스트를 생성해서 쌍을 모두 append 한다. -> [[3, 17], [5, 15], ...]
    # main 에서 리스트[0][0] + 리스트[0][1]을 출력하는걸로,,,!
    global answer_tmp
    if L == 2:
        if sum == n:
            answer_tmp = [prime_list[i] for i in range(len(tmp)) if tmp[i] == True]
            print(f'{n} = {answer_tmp[0]} + {answer_tmp[1]}')

    else:
        for i in range(s, len(prime_list)):
            tmp[i] = True
            combination_with_replacement(L + 1, i + 1, sum + prime_list[i])
            tmp[i] = False


def odd_prime_list(n):
    ch_prime = [True] * (n + 1)
    for i in range(2, int(n ** 1 / 2) + 1):
        if ch_prime[i]:
            for j in range(i + i, n + 1, i):
                ch_prime[j] = False

    return [i for i in range(3, n + 1) if ch_prime[i] == True]


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0: break
        tmp = [False] * (n + 1)
        answer_tmp = []
        prime_list = odd_prime_list(n)
        combination_with_replacement(0, 0, 0)
'''
