def quad():
    n = int(input())
    i = 1
    while n <= i:
        print(i)
        i = i ** 2


def minimum():
    a = int(input())
    i = 2
    while (a % i) != 0:
        i += 1
    print(i)


def degree():
    n = int(input())
    i = 0
    deg = 2
    while deg <= n:
        deg *= 2
        i += 1
    print(i, deg / 2)


def morning_run():
    x = int(input())
    y = int(input())
    i = 1
    while x < y:
        x *= 1.1
        i += 1
    print(i)


def sequence_len():
    x = int(input())
    i = 0
    while x != 0:
        x = int(input())
        i += 1
    print(i)


def sequence_sum():
    x = int(input())
    summary = 0
    while x != 0:
        summary += x
        x = int(input())
    print(summary)


def average():
    x = int(input())
    i = 0
    summary = 0
    while x != 0:
        summary += x
        x = int(input())
        i += 1
    print(summary / i)


def sequence_max():
    a = -1
    maximum = 0
    while a != 0:
        a = int(input())
        if a >= maximum:
            maximum = a
    print(maximum)


def index():
    a = -1
    maximum = 0
    i = 0
    maximum_ind = 0
    while a != 0:
        a = int(input())
        if a > maximum:
            maximum = a
            maximum_ind = i
        i += 1
    print(maximum_ind)


def even_count():
    x = int(input())
    count = 0
    while x != 0:
        if (x % 2) == 0:
            count += 1
        x = int(input())
    print(count)


def count_of_bigger_elements():
    a = int(input())
    i = 0
    while a != 0:
        b = int(input())
        if b > a:
            i += 1
        a = b
    print(i)


def second_max():
    a = int(input())
    prev_maximum = 0
    maximum = 0
    while a != 0:
        if a > maximum:
            prev_maximum = maximum
            maximum = a
        elif a > prev_maximum:
            prev_maximum = a
        a = int(input())
    print(prev_maximum)


def num_of_max():
    a = -1
    maximum = 0
    i = 1
    while a != 0:
        a = int(input())
        if a > maximum:
            maximum = a
            i = 1
        elif a == maximum:
            i += 1
    print(i)


def fibonacci():
    n = int(input())
    f_now = 1
    f_prev = 0
    f_next = 1
    i = 0
    while i != n:
        f_next = f_now + f_prev
        f_prev, f_now = f_now, f_next
        i += 1
    print(f_prev)


def fibonacci_num():
    n = int(input())
    f_now = 1
    f_prev = 0
    f_next = 1
    i = 0
    while f_next <= n:
        f_next = f_now + f_prev
        f_prev, f_now = f_now, f_next
        i += 1
    if f_prev == n:
        print(i)
    else:
        print(-1)


def maximum_of_equal_elements():
    a = int(input())
    record = 1
    prev_record = 1
    while a != 0:
        b = int(input())
        if b == a:
            record += 1
        elif b != a and record < prev_record:
            record = 1
        elif b != a and record >= prev_record:
            prev_record = record
            record = 1
        a = b
    print(prev_record)


def standard_deviation():
    x = -1
    s = 0
    x_n = 0
    x_n_q = 0
    i = 0
    while x != 0:
        x = int(input())
        x_n_q += x ** 2
        x_n += x
        i += 1
    i -= 1
    s = x_n / i
    print(((i * (s ** 2) + x_n_q - 2 * s * x_n) / (i - 1)) ** 0.5)
