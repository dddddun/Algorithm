def solution(n, array):
    dp = [1] * n
    # array를 뒤집어 최장 증가 부분 수열 알고리즘을 사용한다.
    array = array[::-1]

    # LIS 알고리즘 수행
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return len(array) - max(dp)


solution(7, [15, 11, 4, 8, 5, 2, 4])