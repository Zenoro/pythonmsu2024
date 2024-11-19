from fractions import Fraction


class Sausage():
    def __init__(self, intro='pork!', batons=1):
        self.farsh = intro
        self.volume = 12 * Fraction(batons)

    def __abs__(self):
        if self.volume > 0:
            fst, scn = (self.volume/12).as_integer_ratio()
            return "/".join(map(str, (fst, scn))) if scn != 1 else fst
        else:
            return 0

    def __add__(self, other):
        res = Sausage(self.farsh, self.volume / 12)
        if not isinstance(other, Sausage):
            res.volume += other
        else:
            res.volume += other.volume
        return res

    def __sub__(self, other):
        res = Sausage(self.farsh, self.volume / 12)
        if not isinstance(other, Sausage):
            res.volume -= other
        else:
            res.volume -= other.volume
        return res

    def __mul__(self, other):
        res = Sausage(self.farsh, self.volume / 12)
        if not isinstance(other, Sausage):
            res.volume *= other
        else:
            res.volume *= other.volume
        return res
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        res = Sausage(self.farsh, self.volume / 12)
        if not isinstance(other, Sausage):
            res.volume /= other
        else:
            res.volume /= other.volume
        return res

    def __rtruediv__(self, other):
        return self.__div__(other)

    def __bool__(self):
        return bool(abs(self))

    def __str__(self):
        fst, scn = self.volume.as_integer_ratio()
        vol = fst // scn    # количество мясных клеток
        if vol < 0: vol = 0
        newres = ['' for _ in range(5)]
        word = '|'+ (self.farsh * (12//len(self.farsh) + 1))[:12] +'|'

        def SirKolbas(wrd, iskl):
            if vol == 0:
                return iskl
            elif vol % 12 == 0:
                return wrd * (vol // 12)
            else:
                return (wrd * (vol // 12)) + wrd[:(vol % 12)+1] + '|'

        for i in range(5):
            match i:
                case 0:
                # пленка сверху
                    newres[i] = SirKolbas('/'+'-'*12+'\\', '/|')
                case 4:
                # пленка снизу
                    newres[i] = SirKolbas('\\'+'-'*12+'/', '\\|')
                case _:
                # МЯСО
                    newres[i] = SirKolbas(word, '||')
        return '\n'.join(newres)
