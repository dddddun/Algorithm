import sys


def command_program(operation, number):
    global res
    if operation == "add":
        res.add(number)

    elif operation == "remove":
        res.discard(number)

    elif operation == "check":
        if number in res:
            print(1)
        else:
            print(0)

    elif operation == "toggle":
        if number in res:
            res.discard(number)
        else:
            res.add(number)


def solution():
    global res
    m = int(input())
    res = set()

    for i in range(m):
        command = sys.stdin.readline().split()
        if len(command) == 1:
            if command[0] == "all":
                res = set([i for i in range(1, 21)])
            else:
                res = set()
            continue

        operation = command[0]
        number = int(command[1])
        command_program(operation, number)


if __name__ == "__main__":
    solution()
