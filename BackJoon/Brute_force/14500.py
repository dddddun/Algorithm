def check_tet(paper):
    tetromino = [[[0, 1], [0, 2], [0, 3]],
                 [[1, 0], [2, 0], [3, 0]],
                 [[0, 1], [1, 0], [1, 1]],
                 [[1, 0], [2, 0], [2, 1]],
                 [[1, 0], [2, 0], [2, -1]],
                 [[0, 1], [0, 2], [1, 0]],
                 [[0, 1], [0, 2], [1, 2]],
                 [[0, 1], [1, 1], [2, 1]],
                 [[0, 1], [1, 0], [2, 0]],
                 [[0, 1], [0, 2], [-1, 2]],
                 [[1, 0], [1, 1], [1, 2]],
                 [[1, 0], [1, 1], [2, 1]],
                 [[1, 0], [1, -1], [2, -1]],
                 [[0, 1], [-1, 1], [-1, 2]],
                 [[0, 1], [1, 1], [1, 2]],
                 [[0, 1], [0, 2], [1, 1]],
                 [[1, 0], [1, 1], [2, 0]],
                 [[1, 0], [1, -1], [2, 0]],
                 [[0, 1], [0, 2], [-1, 1]]]
    max_sum = 0
    for i in range(n):
        for j in range(m):
            for k in tetromino:
                try:
                    tmp = paper[i][j] + paper[i + k[0][0]][j + k[0][1]] + paper[i + k[1][0]][j + k[1][1]] + paper[i + k[2][0]][j + k[2][1]]
                except:
                    tmp = 0
                max_sum = max(max_sum, tmp)
    return max_sum


if __name__ == "__main__":
    n, m = map(int, input().split())
    paper = []
    for _ in range(n):
        paper.append(list(map(int, input().split())))

    answer = check_tet(paper)
    print(answer)
