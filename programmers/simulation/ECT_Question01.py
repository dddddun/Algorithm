knight = input()
dict_row = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

column = int(knight[1])
row = int(dict_row[knight[0]])
cnt = 0

dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]

for i in range(8):
    ch_column = column + dx[i]
    ch_row = row + dy[i]

    if ch_column in range(1, 9) and ch_row in range(1, 9):
        cnt += 1

print(cnt)
