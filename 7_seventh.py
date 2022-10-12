def even_index():
    a = input().split()
    for i in range(int((len(a) + 1) / 2)):
        print(a[i * 2])


def even_elements():
    a = input().split()
    for x in a:
        if (int(x) % 2) == 0:
            print(x)


def bigger_than_prev():
    a = input().split()
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            print(a[i])


def neighbors():
    a = input().split()
    b = [a[i][:-1] for i in range(len(a))]
    for i in range(1, len(b)):
        if b[i] == b[i - 1]:
            print(a[i - 1], a[i])
            break


def bigger_than_neighbors():
    a = input().split()
    c = 0
    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            c += 1
    print(c)


def maximum():
    a = [int(i) for i in input().split()]
    max_a = max(a)
    i = 0
    for x in a:
        if maximum == x:
            print(max_a, i)
            break
        i += 1


def line():
    a = [int(i) for i in input().split()]
    a_sorted = []
    h = int(input())
    c = 1
    for i in range(len(a)):
        minimal = max(a)
        a_sorted.append(minimal)
        a[a.index(minimal)] = 0
    for x in a_sorted:
        if h <= x:
            c += 1
    print(c)


def count_of_elements():
    a = [int(i) for i in input().split()]
    b = a[::-1]
    count = 0
    i = 0
    while a:
        count += 1
        end = b.index(a[0])
        a = a[len(a) - end:]
        b = b[:end]
        i += 1
    print(count)


def neighbors_replacement():
    a = [i for i in input().split()]
    for i in range(0, int(len(a) / 2) * 2, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
    print(' '.join(a))


def min_max():
    x = [int(i) for i in input().split()]
    minimal, maximal = min(x), max(x)
    a, b = x.index(minimal), x.index(maximal)
    x[a], x[b] = x[b], x[a]
    print(' '.join([str(i) for i in x]))


def delete_element():
    a = [i for i in input().split()]
    k = int(input())
    print(' '.join(a[:k]), ' '.join(a[k + 1:]))


# Задача «Вставить элемент»
'''Условие
Дан список целых чисел, число k и значение C. 
Необходимо вставить в список на позицию с индексом k элемент,
равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается,
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, 
не делая этого при выводе и не создавая дополнительного списка.'''


def insert_element():
    a = [i for i in input().split()]
    a.append('')
    k = [int(i) for i in input().split()]
    for i in range(len(a) - 1, k[0], -1):
        a[i] = a[i - 1]
    a[k[0]] = str(k[1])
    print(' '.join(a))


# Задача «Количество совпадающих пар»
'''Условие
Дан список чисел. 
Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.'''


def pair_count():
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                count += 1
    print(count)


# Задача «Уникальные элементы»
'''Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке.'''


def unique_elements():
    a = [int(i) for i in input().split()]
    for i in range(len(a)):
        a_slice = a.index(a[i]) + 1
        if a[i] not in a[a_slice:]:
            print(a[i])


# Задача «Кегельбан»
'''Условие
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. 
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. 
Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, 
где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.'''


def bowling_alley():
    data = [int(i) for i in input().split()]
    out = ['I' for _ in range(data[0])]
    for i in range(data[1]):
        i = [int(i) for i in input().split()]
        for j in range(i[1] - i[0] + 1):
            out[i[0] + j - 1] = '.'
    print(''.join(out))


# Задача «Ферзи»
'''Условие
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.'''


def queens():
    x = []
    y = []
    out = False
    for i in range(8):
        i = [int(i) for i in input().split()]
        x.append(i[0])
        y.append(i[1])
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                out = True
                break
    if out is False:
        print('NO')
    else:
        print('YES')
