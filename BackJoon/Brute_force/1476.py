def count_day(today):
    E, S, M = today[0], today[1], today[2]
    e, s, m, cnt = 0, 0, 0, 0
    cnt = 0
    while True:
        if e == E and s == S and m == M:
            return cnt

        cnt += 1
        e += 1
        s += 1
        m += 1

        if e == 16: e = 1
        if s == 29: s = 1
        if m == 20: m = 1


if __name__ == "__main__":
    today = list(map(int, input().split()))
    print(count_day(today))