def BiquadEquation(a:int|float, b:int|float, c:int|float) -> str:
    quad, biquad = [], []
    sqrter = lambda x: [-x**0.5, x**0.5] if x > 0 else [x]

    if a != 0:
        disc = (b**2-4*a*c)**0.5
        if disc >= 0:
            t1, t2 = (-b - disc) / (2*a), (-b + disc) / (2*a)
            if t1 != t2 and t1 >= 0:
                quad.append(t1)
            if t2 >= 0:
                quad.append(t2)
            else:
                quad.append(0)
        else:
            return [0]
    elif b != 0:
        if -c / b <0:
            return [0]
        else:
            quad.append(-c / b)
    else:
        return [-1] if c == b else [0]

    for elem in quad:
        biquad += sqrter(elem)
    return sorted(biquad)


if __name__ == '__main__':
    a,b,c = map(int, input().split(','))
    print(*BiquadEquation(a,b,c))
