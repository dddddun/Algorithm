# bisect모듈을 사용하지 않고 문제를 해결하는 경우
def start_binary(lt, rt, target, array):
    while lt <= rt:
        mid = (lt + rt) // 2
        if array[mid] == target and (array[mid - 1] < target or mid == 0):
            return mid
        elif array[mid] < target:
            lt = mid + 1
        elif array[mid] >= target:
            rt = mid - 1


def end_binary(lt, rt, target, array):
    while lt < rt:
        mid = (lt + rt) // 2
        if array[mid] == target and (array[mid + 1] > target or mid == len(array) - 1):
            return mid + 1
        elif array[mid] <= target:
            lt = mid + 1
        elif array[mid] > target:
            rt = mid - 1


def solution(n, x, nums):
    lt = 0
    rt = n - 1

    start = start_binary(lt, rt, x, nums)

    if start is None:
        # print(0)
        return 0

    end = end_binary(lt, rt, x, nums)

    # print(end - start)
    return end - start


# bisect 모듈을 사용하는 경우
from bisect import bisect_left, bisect_right


def solution(n, x, nums):
    start = bisect_left(nums, x)
    if start is None:
        return 0
    end = bisect_right(nums, x)

    # print(end - start)
    return end - start


solution(7, 2, [1, 1, 2, 2, 2, 2, 3])
solution(7, 4, [1, 1, 2, 2, 2, 2, 3])
