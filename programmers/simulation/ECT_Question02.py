n, m = map(int, input().split())
now = list(map(int, input().split()))

# x, y, direction = map(int, input().split())
x = now[1]
y = now[0]
direction = now[2]
# 0:북, 1:동, 2:남, 3:서
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
_map = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
res = 1

while True:
    if cnt == 4:
        ch_x = x - dx[direction]
        ch_y = y - dy[direction]

        # 맵의 외곽으로 떨어지는 경우는 코딩테스트에서 고려하지 않아도 된다!!!!!!!! 아랫줄 필요없음!
        if 0 <= ch_x < n and 0 <= ch_y < m:
            if _map[ch_x][ch_y] == 0:
                x = ch_x
                y = ch_y
                _map[x][y] = 1
                cnt = 0
            else:
                break
        else:
            break

    ch_x = x + dx[direction]
    ch_y = y + dy[direction]

    # 여기도 필요하지 않음!
    if 0 <= ch_x < n and 0 <= ch_y < m:
        if _map[ch_x][ch_y] == 0:
            x = ch_x
            y = ch_y
            _map[x][y] = 1
            direction += 1
            if direction == 4:
                direction = 0
            cnt = 0
            res += 1
        else:
            direction += 1
            if direction == 4:
                direction = 0
            cnt += 1

    else:
        direction += 1
        if direction == 4:
            direction = 0
        cnt += 1

print(res)




