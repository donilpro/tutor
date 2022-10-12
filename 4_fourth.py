def row_1():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        print(i)


def row_2():
    a = int(input())
    b = int(input())
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, - 1):
            print(i)


def row_3():
    a = int(input())
    b = int(input())
    for i in range(a - (a + 1) % 2, b - b % 2, -2):
        print(i)


def tenth_sum():
    summary = 0
    for i in range(10):
        i = int(input())
        summary = summary + i
    print(summary)


def n_numbers():
    summary = 0
    for i in range(n):
        i = int(input())
        summary = summary + i
    print(summary)


def cubes():
    n = int(input())
    summary = 0
    for i in range(1, n + 1):
        summary = summary + i ** 3
    print(summary)


def factorial():
    n = int(input())
    fact = 1
    for i in range(1, n + 1):
        fact = i * fact
    print(fact)


def sum_factorial():
    n = int(input())
    fact = 1
    summary = 0
    for i in range(0, n):
        fact = (i + 1) * fact
        summary += fact
    print(summary)


def zeros():
    n = int(input())
    summary = 0
    for i in range(n):
        i = int(input())
        if i == 0:
            summary += 1
    print(summary)


def stairs():
    n = int(input())
    out = ''
    for i in range(1, n + 1):
        out += str(i)
        print(out)


def card():
    n = int(input())
    f_summary = 0
    s_summary = 0
    for i in range(1, n + 1):
        f_summary += i
    for i in range(n - 1):
        i = int(input())
        s_summary += i
    print(f_summary - s_summary)
