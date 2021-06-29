def pre_permutation(n, per):
    # 역배열(내림차순)을 깨는 최초의 인덱스
    first_idx = 0

    # 최초의 인덱스 탐색
    for i in range(n - 1, 0, -1):
        if per[i] < per[i - 1]:
            first_idx = i - 1
            # 최초의 인덱스보다 큰 인덱스의 요소들 뒤집기
            per = per[:first_idx + 1] + per[n - 1:first_idx:-1]
            break
    else:
        return -1

    # 뒤집은 요소들 중 최초의 인덱스 다음으로 작은 수와 최초의 인덱스 스왑
    for i in range(first_idx + 1, n):
        if per[first_idx] > per[i]:
            per[first_idx], per[i] = per[i], per[first_idx]
            return per


def solution(n, per):
    answer = pre_permutation(n, per)
    if answer == -1:
        print(answer)
    else:
        print(*answer)


if __name__ == "__main__":
    N = int(input())
    permutation = list(map(int, input().split()))
    solution(N, permutation)