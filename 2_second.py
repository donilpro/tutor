def minimum_two():
    a = int(input())
    b = int(input())
    if a < b:
        print(a)
    else:
        print(b)


def sign():
    x = int(input())
    if x > 0:
        print(1)
    elif x < 0:
        print(-1)
    else:
        print(0)


def chess():
    f_x = int(input())
    f_y = int(input())
    s_x = int(input())
    s_y = int(input())
    if (f_x + f_y) % 2 == (s_x + s_y) % 2:
        print('YES')
    else:
        print('NO')


def year():
    year = int(input())
    if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0:
        print('YES')
    else:
        print('NO')


def minimum_three():
    a = int(input())
    b = int(input())
    c = int(input())
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)


def how_much():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b or b == c or a == c:
        if a == b and b == c and a == c:
            print(3)
        else:
            print(2)
    else:
        print(0)


def rook():
    f_x = int(input())
    f_y = int(input())
    s_x = int(input())
    s_y = int(input())
    if f_x == s_x or f_y == s_y:
        print('YES')
    else:
        print('NO')


def king():
    f_x = int(input())
    f_y = int(input())
    s_x = int(input())
    s_y = int(input())
    if abs(f_x - s_x) > 1 or abs(f_y - s_y) > 1:
        print('NO')
    else:
        print('YES')


def bishop():
    f_x = int(input())
    f_y = int(input())
    s_x = int(input())
    s_y = int(input())
    if abs(f_x - s_x) == abs(f_y - s_y):
        print('YES')
    else:
        print('NO')


def queen():
    f_x = int(input())
    f_y = int(input())
    s_x = int(input())
    s_y = int(input())
    if abs(f_x - s_x) == abs(f_y - s_y):
        print('YES')
    elif f_x == s_x or f_y == s_y:
        print('YES')
    else:
        print('NO')


def knight():
    f_x = int(input())
    f_y = int(input())
    s_x = int(input())
    s_y = int(input())
    if abs(f_x - s_x) == 2 and abs(f_y - s_y) == 1:
        print('YES')
    elif abs(f_x - s_x) == 1 and abs(f_y - s_y) == 2:
        print('YES')
    else:
        print('NO')


def chocolate():
    n = int(input())
    m = int(input())
    k = int(input())
    s = n * m
    if k <= s and (k >= n or k >= m) and (k % n == 0 or k % m == 0):
        print('YES')
    else:
        print('NO')


def pool():
    N = int(input())
    M = int(input())
    x = int(input())
    y = int(input())
    if N < M:
        N, M = M, N
    x_rev = abs(M - x)
    y_rev = abs(N - y)
    if y < x and y < y_rev and y < x_rev:
        print(y)
    elif y_rev < x and y_rev < y and y_rev < x_rev:
        print(y_rev)
    elif x_rev < x and x_rev < y and x_rev < y_rev:
        print(x_rev)
    else:
        print(x)
    