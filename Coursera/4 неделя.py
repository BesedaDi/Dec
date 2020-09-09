# минимум 4 чисел
a, b, c, d = int(input()), int(input()), int(input()), int(input())


def min4(a, b, c, d):
    min_min1 = min(a, b)
    min_min2 = min(c, d)
    print(min(min_min1, min_min2))


min4(a, b, c, d)
# длина отрезка
import math

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())


def distance(x1, y1, x2, y2):

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(dist)


distance(x1, y1, x2, y2)
# периметр треугольника
import math

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())


def P(x1, y1, x2, y2, x3, y3):
    dist_12 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    dist_13 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    dist_23 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    print(dist_12 + dist_13 + dist_23)


P(x1, y1, x2, y2, x3, y3)
# принадлежит ли точка квадрату-1
def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


x, y = float(input()), float(input())

if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
# принадлежит ли точка2
def IsPointInSquare(x, y):
    return 0 <= abs(x) + abs(y) <= 1


x, y = float(input()), float(input())

if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
# принадлежит ли кругу
import math


def IsPointCircle(x, y, xc, yc, r):
    dist = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)
    return dist <= r


x, y = float(input()), float(input())
xc, yc = float(input()), float(input())
r = float(input())

if IsPointCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
# минимальный делитель числа
import math

n = int(input())


def MinDivisor(n):
    m = 2
    while n % m != 0:
        m += 1
        if m > math.sqrt(n):
            return n
    return m
# проверка числа на простоту
n = int(input())
import math

def IsPrime(n):
    i = 2
    while n % i != 0:
        for _ in range(math.sqrt(n)):
            s = n % i
        i += 1
    if i == n:
        print('YES')
    else:
        print('NO')


IsPrime(n)

# возведение в степень
a, n = float(input()), int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n != 0:
        return a * a ** (n - 1)
        power(a, n)


print(power(a, n))
# отрицательная степень
a, n = float(input()), int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n != 0:
        return a * a ** (n - 1)
        power(a, n)
    elif n < 0:
        return 1 / (a * a ** (n - 1))
        power(a, n)


print(power(a, n))
# сложение без сложения
a, b = int(input()), int(input())


def sum(a, b):
    if a != 0 and b != 0:
        return (a + 1) - 1 + (b + 1) - 1
        sum(a, b)
    elif a == 0:
        return b
    elif b == 0:
        return a


print(sum(a, b))
# быстрое возведение в степень
a, n = float(input()), int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        if n != 0:
            return (a ** 2) ** (n / 2)
            power(a, n)
    elif n % 2 != 0:
        if n != 0:
            return a * a ** (n - 1)
            power(a, n)


print(power(a, n))
# алгоритм евклида
a, b = int(input()), int(input())


def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
        gcd(b, a % b)
    else:
        return a


print(gcd(a, b))
# сократите дроби
def gcd(n, m):
    if m != 0:
        return gcd(m, n % m)
        gcd(b, n % b)
    else:
        return n


n, m = int(input()), int(input())


def ReduceFraction(n, m):
    if m != 0:
        k = gcd(m, n % m)
        p = n // k
        q = m // k
        return p, q
        ReduceFraction(n, m)
    else:
        return p, q


print(*ReduceFraction(n, m))
# число фибоначи
n = int(input())
m = 0


def phib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)
        phib(n)


print(phib(n))
# число сочетаний
n, k = int(input()), int(input())


def C(n, k):
    if k == 1:
        return n
    elif (n == k and n != 0) or k == 0:
        return 1
    elif n == 0 and k == 0:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)
        C(n, k)


print(C(n, k))
# сумма последовательности
def sum():
    n = int(input())
    if n == 0:
        return 0
    elif n != 0:
        return n + sum()


print(sum())
#
