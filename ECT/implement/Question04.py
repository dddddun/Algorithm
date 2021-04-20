def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 자물쇠 중앙 부분에 기존 자물쇠 값 입력
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 키를 회전시킨다
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        # 확장된 자물쇠의 영역에 key의 값을 더한다.
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 기존 자물쇠의 영역을 확인하여 전부 1이면 True를 반환한다.
                if check(new_lock):
                    return True

                # check 한 결과 모두 1이 아니면 더해준 key값을 다시 빼준다.
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    # 모든 경우를 탐색한 결 True 가 나오지 않는다면 False
    return False


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])