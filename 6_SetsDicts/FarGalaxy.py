from math import hypot
import sys


def distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Find distance between two galaxies with XYZ coordinates"""
    return hypot((x1-x2), (y1-y2), (z1-z2))


if __name__ == "__main__":
    # input data about galaxies
    s = [[list(map(float, foo[:-1])), foo[-1]] for el in sys.stdin.readlines() if len(foo:=el.split()) > 3]

    # find max distance
    maxdistance = 0
    res = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if (k := distance(*(s[i][:-1][0]), *(s[j][:-1][0]))) > maxdistance:
                maxdistance = k
                res = [s[i][-1], s[j][-1]]

    print(' '.join(sorted(res)))
