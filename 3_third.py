def last():
    a = int(input())
    b = int(a / 10)
    print(a - b * 10)


def moscow():
    v = int(input())
    t = int(input())
    s = v * t
    print(s % 109)


def fraction():
    x = float(input())
    print(x - int(x))


def f_dot():
    x = float(input())
    print(int(x * 10) % 10)


def ending():
    n = int(input())
    if n == 1:
        end = 45
    elif n % 2 == 0:
        end = n * 45 + n / 2 * 5 + (n - 2) / 2 * 15
    else:
        end = n * 45 + (n - 1) / 2 * 15 + (n - 1) / 2 * 5
    print(((540 + end) // 60), ' ', ((540 + end) % 60))


def car():
    import math

    n = int(input())
    m = int(input())
    print(math.ceil(m / n))


def money():
    a = int(input())
    b = int(input())
    n = int(input())
    cost = (a * 100 + b) * n
    print(cost // 100, ' ', cost % 100)


def time():
    f_h = int(input())
    f_m = int(input())
    f_s = int(input())
    s_h = int(input())
    s_m = int(input())
    s_s = int(input())
    f_time = f_h * 3600 + f_m * 60 + f_s
    s_time = s_h * 3600 + s_m * 60 + s_s
    print(s_time - f_time)


def snail():
    h = int(input())
    a = int(input())
    b = int(input())
    print(int(1 + (h - b - 1) / (a - b)))


def tenth():
    x = int(input())
    print(int(x // 10 % 10))


def summary():
    x = int(input())
    c = x % 10
    b = (x % 100 - c)
    a = x - b - c
    print(a / 100 + b / 10 + c)


def hypotenuse():
    a = int(input())
    b = int(input())
    print((a ** 2 + b ** 2) ** (1 / 2))


def clocks_1():
    h = int(input())
    m = int(input())
    s = int(input())
    h_d = 30 * h
    m_d = 30 * m / 60
    s_d = 30 * s / 3600
    print(h_d + m_d + s_d)


def clocks_2():
    h_d = float(input())
    print(h_d * 12 % 360)


def clocks_3():
    h_d = float(input())
    total = h_d * 120
    h = int(total // 3600)
    m = int(total - h * 3600)
    s = int(m % 60)
    print(h, m // 60, s)


def percent():
    p = int(input())
    x = int(input())
    y = int(input())
    s = int((x * 100 + y) * (p + 100) / 100)
    print(s // 100, s % 100)
    