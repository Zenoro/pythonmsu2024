def sheff(A, B):
    if not A and not B:
        return True
    elif A and B:
        return False
    else:
        return A if not B else B

