def next_permutation(n, per):
    # 역배열을 깨는 최초의 인덱스
    first_idx = 0

    # 역배열을 깨는 최초의 인덱스 탐색
    for i in range(n - 1, 0, -1):
        if per[i] > per[i - 1]:
            first_idx = i - 1
            break

    # i보다 큰 인덱스 중 최초의 수 바로 다음 큰 수를 찾고 최초의 수와 스왑
    for i in range(n - 1, 0, -1):
        if per[first_idx] < per[i]:
            per[first_idx], per[i] = per[i], per[first_idx]
            # i 인덱스 이후의 순열을 뒤집기
            per = per[:first_idx + 1] + per[n - 1:first_idx:-1]
            # per = per[:first_idx + 1] + sorted(per[first_idx+1:])
            return per
    else:
        return -1


def solution(n, permutation):
    answer = next_permutation(n, permutation)
    if answer == -1:
        print(answer)
    else:
        print(*answer)


if __name__ == "__main__":
    n = int(input())
    permutation = list(map(int, input().split()))
    solution(n, permutation)