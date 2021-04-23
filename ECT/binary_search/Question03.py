def binary(lt, rt, array, c):
    max_dist = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        current = array[0]
        cnt = 1
        for i in range(1, len(array)):
            if array[i] >= current + mid:
                cnt += 1
                current = array[i]
        if cnt >= c:
            max_dist = mid
            lt = mid + 1
        else:
            rt = mid - 1

    return max_dist



def solution(n, c, homes):
    homes.sort()
    max_dist = homes[-1] - homes[0]
    min_dist = homes[1] - homes[0]
    answer = binary(min_dist, max_dist, homes, c)

    # print(answer)
    return answer



solution(5, 3, [1, 2, 8, 4, 9])