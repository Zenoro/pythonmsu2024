LENMAX = 101


def countSort(count_arr: list[int]):
    # out = []
    i = 0
    while i < LENMAX:
        if count_arr[i]:
            yield i
            # out.append(i)
            count_arr[i] -= 1
            i -= 1
        i += 1
    # return out


if __name__ == "__main__":
    dd = dict()
    while s := input():
        x, y = eval(s)
        if not dd.get(x, 0):
            dd[x] = [0 for _ in range(LENMAX)]
        dd[x][y] += 1

    for elem in sorted(list(dd.keys())):
        for scndelem in countSort(dd[elem]):
            print(elem, ', ', scndelem, sep='')
