# 재귀함수를 사용해 순열 출력하기
def dfs(L, ch, permutation, n):
    if L == n:
        for i in range(n):
            print(permutation[i], end=' ')
        print()

    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                permutation[L] = i
                dfs(L + 1, ch, permutation, n)
                ch[i] = 0


def solution(n):
    ch = [0] * (n + 1)
    permutation = [0] * n
    dfs(0, ch, permutation, n)


if __name__ == "__main__":
    N = int(input())
    solution(N)