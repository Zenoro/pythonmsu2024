def BinPow(a: object, n: object, func:callable):
    return a if n == 1 else func(BinPow(a,n // 2, func),
                                 BinPow(a, n // 2, func)) if n % 2 == 0 else func(BinPow(a, n - 1,
                                                                                         func), a)
