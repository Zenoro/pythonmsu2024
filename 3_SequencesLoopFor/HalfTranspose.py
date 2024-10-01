fst = list(map(int, input().split(',')))
leng = len(fst)
alls = [fst] + [list(map(int, input().split(','))) for _ in range(leng-1)]

for i in range(len(alls)):
    uptodown, lefttoright = [], []
    for j in range(i):
        lefttoright.append(str(alls[i][j]))
        uptodown.append(str(alls[j][i]))
    print(','.join(lefttoright + [str(alls[i][i])] + uptodown[::-1]))
