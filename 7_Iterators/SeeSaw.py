from itertools import zip_longest

def seesaw(nums: iter) -> iter:
    to2, no2 = [], []    
    for elem in nums:
        if elem % 2 == 0:
            to2.append(elem)
        else:
            no2.append(elem)
    for x,y in zip_longest(to2, no2):
        match x,y:
            case _, None:
                yield x
            case None, _:
                yield y
            case _:
                yield x
                yield y


# print(*seesaw(i//3 for i in range(1, 27, 2)))
