def solution(n, edge):
    dic = dict()
    for start, end in edge:
        dic[start] = dic.get(start, 0) + [end]
    print(dic)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])