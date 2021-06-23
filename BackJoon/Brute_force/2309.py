def remove_dwarfs(dwarfs):
    sum_weight = sum(dwarfs)
    for i in range(9):
        for j in range(i+1, 9):
            if 100 == sum_weight - (dwarfs[i] + dwarfs[j]):
                del dwarfs[j]
                del dwarfs[i]
                # first, second = dwarfs[i], dwarfs[j]
                # dwarfs.remove(first)
                # dwarfs.remove(second)
                return dwarfs


if __name__ == "__main__":
    dwarfs = [int(input()) for _ in range(9)]
    dwarfs.sort()
    remove_dwarfs(dwarfs)
    for dwarf in dwarfs:
        print(dwarf)

