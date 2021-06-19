if __name__ == "__main__":
    _string = input()
    target = input()
    answer = []
    for s in _string:
        answer.append(s)
        if answer[-1] == target[-1] and ''.join(answer[-len(target):]) == target:
            del answer[-len(target):]
    if len(answer) == 0:
        print("FRULA")
    else:
        print("".join(answer))



# 시간초과
'''
def explode(_string, target):
    _string = _string.replace(target, "")
    return _string


if __name__ == "__main__":
    _string = input()
    target = input()
    while True:
        _string = explode(_string, target)
        if len(_string) == 0:
            print("FRULA")
        if _string.find(target) == -1:
            break

    print(_string)
'''
