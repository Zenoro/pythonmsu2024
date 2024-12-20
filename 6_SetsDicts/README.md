## [PairNumber - 'Количество пар'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_PairNumber)

Вводится текст, состоящий из «слов» (последовлательностей непробельных символов), разделённых последовательностями пробельных символов. Последня строка пустая. Посчитать и вывести, сколько различных последовательных пар слов (без учёта порядка) встречается в тексте.


**Input:**

    qwe rty asd
    rty qwe asd
    wat qwe wat


**Output:**

    5

## [ThreeSquares - 'Три квадрата'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_ThreeSquares)

Ввести произвольную последовательность (не обязательно кортеж) натуральных чисел, не превышающих 200000. Вывести, сколько среди них различных чисел, являющихся суммой трёх квадратов натуральных чисел.

*Пояснение. Входная последовательность должна обрабатываться так: seq = set(eval(input()))*

**Input:**

    3, 4, 2, 9, 1, 5, 6, 7, 8, 3, 6

**Output:**

    3

## [FarGalaxy - 'В далёкой галактике'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_FarGalaxy)

Ввести построчно четвёрки вида «число число число слово», где первые три числа — это координаты галактики по имени «слово» (некоторые галактики могут называться одинаково, но координаты у всех разные). Последняя строка ввода не содержит пробелов и не учитывается. Вывести в алфавитном порядке имена любых двух наиболее удалённых друг от друга галактик. Считается, что одинаковых расстояний в списке нет.

**Input:**

    35.764 -797.636 -770.320 almost
    88.213 -61.688 778.457 gene
    -322.270 -248.555 -812.730 trend
    721.262 630.355 968.287 dow
    -895.519 -970.173 97.282 non
    -561.036 -350.840 -723.149 disco
    -151.546 -900.962 -658.862 bidder
    -716.197 478.576 -695.843 hawaii
    -744.664 -173.034 -11.211 sad
    -999.968 990.467 650.551 erik
    .

**Output:**

    almost erik


## [PokeMon - 'Покемоны'](https://uneex.org/LecturesCMC/PythonIntro2024/Homework_PokeMon)

Участники некоторой карточной игры владеют несколькими колодами, из которых они составляют пачку — набор попарно различающихся карт. Каждая колода имеет номер; колоды с одинаковыми номерами содержат совпадающие наборы карт. Ввести строки вида "имя игрока / номер колоды" (колода принадлежит игроку) или "номер колоды / название карты" (карта входит в колоду); последняя строка пустая. Вывести в алфавитном порядке имена всех игроков, чья пачка наибольшая. Имена игроков и названия карт не могут начинаться с цифры.
    
**Input:**

    0 / Misdreavus
    Svjatoslav Devjatkov / 3
    2 / Yamask
    Vsevid Mladenov / 1
    1 / Keldeo
    0 / Keldeo
    1 / Misdreavus
    2 / Scatterbug
    0 / Crawdaunt
    2 / Keldeo
    1 / Vanillite
    Svjatoslav Devjatkov / 0
    2 / Gardevoir
    Neljub Mstislavin / 2
    2 / Crawdaunt
    0 / Yamask
    3 / Reshiram

**Output:**

    Neljub Mstislavin
    Svjatoslav Devjatkov
