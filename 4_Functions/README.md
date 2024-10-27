## [ShefferStroke - 'Штрих Шеффера'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_ShefferStroke)

Написать функцию `sheff(A, B)`, реализующую логическую операцию [Штрих Шеффера](https://ru.wikipedia.org/wiki/%D0%A8%D1%82%D1%80%D0%B8%D1%85%20%D0%A8%D0%B5%D1%84%D1%84%D0%B5%D1%80%D0%B0) `A ↑ B` по следующему принципу:

* Если *ровно один* из операндов не пуст, возвращается этот операнд
* Если оба операнда пусты, возвращается `True`
* Если оба операнда непусты, возвращается `False` 
    
**Input:**

    print(sheff(1, 2))
    print(sheff([], 1.1))
    print(sheff((0, 0), ""))

**Output:**

    False
    1.1
    (0, 0)

* <!> Это очень простая функция, так что необязательное упражнение: минимизировать количество символов (пробелы и переводы строки не в счёт). В моём решении их 47, и я уверен, что это далеко не предел! 

## [DivDigit - 'Цифроделители'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_DivDigit)

Написать функцию `divdigit(N)`, которой передаётся произвольное натуральное число N, а в ответ функция возвращает количество цифр этого числа, являющихся её делителями.

**Input:**

    print(divdigit(312345))

**Output:**

    4

## [BinPow - 'Бинарное возведение в степень'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_BinPow)

Написать функцию `BinPow()`, которая принимает три параметра: python3-объект `a`, натуральное число `0<N<1000000`, и некоторую ассоциативную бинарную функцию `f()`. Функция `BinPow()` реализует алгоритм [бинарного возведения в степень](http://e-maxx.ru/algo/binary_pow) (кроме нулевой степени). Результатом `BinPow(a, n, f)` будет применение `f(x)` к `a` `n-1` раз.

**Input:**

    print(BinPow(2, 33, lambda a, b: a * b), 2**33)
    print(BinPow("Se", 7, str.__add__))

**Output:**

    8589934592 8589934592
    SeSeSeSeSeSeSe

## [FunVect - 'Вектор функций'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_FunVect)

Написать функцию `superposition(funmod, funseq)`, которая принимает два параметра — функцию `funmod()` от одного переменного, и последовательность `funseq[]` функций от одного переменного. `superposition()` возвращает также список функций `funres[]`, каждая из которых представляет собой суперпозицию вида `funres[i](x) ≡ funmod(funseq[i](x))`

**Input:**

    from math import *
    F, G = superposition(abs, (sin, cos))
    print(F(-1), G(-1), F(2), G(2))

**Output:**

    0.8414709848078965 0.5403023058681398 0.9092974268256817 0.4161468365471424
