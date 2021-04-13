def solution(arrows):
    def get_to(curr, move):
        x, y = curr
        x = curr[0] + (move in [1,2,3]) + -1*(move in [5,6,7])
        y = curr[1] + (move in [0,1,7]) + -1*(move in [3,4,5])
        return (x, y)
    def get_crossed(line):
        x1,y1 = line[0]
        x2,y2 = line[1]
        return tuple(sorted([(x1+1,y1), (x2-1,y2)]))

    rooms = 0
    curr = (0,0)
    lines = set()
    passed = set()
    passed.add(curr)
    for move in arrows:
        to = get_to(curr, move)
        line = tuple(sorted([curr, to]))
        if line in lines:
            curr = to
            continue
        elif to in passed:
            lines.add(line)
            rooms += 1
        else:
            lines.add(line)
            passed.add(to)
        # any line crossed?
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            if get_crossed(line) in lines:
                rooms += 1
        curr = to
    return rooms