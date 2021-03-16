def solution(name):
    up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    down = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ch = [0] * len(name)
    cnt = 0
    i = 0

    while sum(ch) != len(name):
        if name[i] == 'A' and ch[i] == 0:
            a = i
            b = i
            left_cnt = 0
            right_cnt = 0

            while name[a] != 'A':
                a += 1
                left_cnt += 1
            while name[b] != 'A':
                b -= 1
                right_cnt += 1
            if left_cnt <= right_cnt:
                i = a
                cnt += left_cnt
                ch[i] = 1
            else:
                i = b
                cnt += right_cnt
                ch[i] = 1
        else:
            cnt += 1
            if name[i] in up:
                cnt += (ord('M') - ord(name[i]))
                ch[i] = 1
                i += 1
            elif name[i] in down:
                cnt += (ord('Z') - ord(name[i]))
                ch[i] = 1
                i += 1

    return cnt

