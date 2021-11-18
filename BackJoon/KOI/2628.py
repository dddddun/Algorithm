def find_max_len(nums):
    maximum_value = 0
    nums.sort()

    for i in range(len(nums)-1):
        maximum_value = max(maximum_value, nums[i+1] - nums[i])
    return maximum_value


if __name__ == "__main__":
    n, m = map(int, input().split())
    hor = [0, n]
    ver = [0, m]
    num = int(input())

    for i in range(num):
        type, cut_num = map(int, input().split())
        if type == 0:
            ver.append(cut_num)
        else:
            hor.append(cut_num)

    max_hor = find_max_len(hor)
    max_ver = find_max_len(ver)

    print(max_ver * max_hor)