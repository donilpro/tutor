def sum_of_three():
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b + c)


def square():
    b = int(input())
    h = int(input())
    print(b * h / 2)


def apples():
    n = int(input())
    k = int(input())
    print(k // n)
    print(k % n)


def clock():
    n = int(input())
    h = n // 60
    print(h % 24)
    print((n - h * 60) % 60)


def hello():
    name = input()
    print('Hello, ' + name + '!')


def next_prev():
    n = int(input())
    next = n + 1
    prev = n - 1
    print('The next number for the number ' + str(n) + ' is ' + str(next))
    print('The previous number for the number ' + str(n) + ' is ' + str(prev))


def parts():
    f_class = int(input())
    s_class = int(input())
    t_class = int(input())
    print((f_class // 2 + f_class % 2) + (s_class // 2 + s_class % 2) + (t_class // 2 + t_class % 2))


def boots():
    a = int(input())
    b = int(input())
    l = int(input())
    N = int(input())
    length = l * 2 + (N - 1) * (b + a) * 2 + a
    print(length)
