import copy

class vector():
    def __init__(self, mas):
        self.mas = list(mas)

    def __iter__(self):
        for elem in self.mas:
            yield elem

    def __add__(self, other):
        if not isinstance(other, vector):
            return self + vector(other)
        else:
            res = [self.mas[i] + other.mas[i] for i in range(len(self.mas))]
        return vector(res)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __matmul__(self, other):
        if not isinstance(other, vector):
            return self @ vector(other)
        else:
            return sum([self.mas[i] * other.mas[i] for i in range(len(self.mas))])

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __str__(self):
        return ":".join(map(str, self.mas))
