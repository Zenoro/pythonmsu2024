def divdigit(N: int) -> int:
    return sum([1 for i in str(N) if (k:=int(i)) != 0 and N % k == 0])