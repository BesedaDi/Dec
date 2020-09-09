n = int(input())
s1 = n // 10
s1 = s1 % 10
print(s1)
n = int(input())
s = n // 10
s = s // 10
s1 = n // 10
s1 = s1 % 10
s3 = n % 10
print(s+s1+s3)
print('A'*100, end='')
# задача про часы
n = int(input())
print((n // 60) % 24, n % 60)
# стоимость покупок
a = int(input())
b = int(input())
n = int(input())
s = n * (a*100 + b)
s1 = s // 100
s2 = s % 100
print(s1, s2)
# следующая и предыдущая
n = int(input())
print('The next number for the number', n, 'is', n+1, end='.')
print()
print('The previous number for the number', n, 'is', n-1, end='.')
# 0 в 1, и 1 в 0.
n = int(input())
print(n % 1 // 1)
# следующее четное
n = int(input())
print((((n+n)//n))+n)
# 100 подряд в квадрат
n = input()
s = int(n*100)
s = s**2
print(s)
# максимум их двух
a = int(input())
b = int(input())
if a <= b:
    print(b)
elif a > b:
    print(a)
# какое число больше
a = int(input())
b = int(input())
if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)
# максимум трех чисел
a = int(input())
b = int(input())
c = int(input())
if a >= b:
    if c > a:
        print(c)
    else:
        print(a)
else:
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else:
            print(c)
# високосный год
a = int(input())
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print('YES')
else:
    print('NO')
# ход короля
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1+1 == b1 and a2+1 == b2:
    print('YES')
elif a2 == b2 and a1+1 == b1:
    print('YES')
elif a2 == b2 and a1-1 == b1:
    print('YES')
elif a1 == b1 and a2+1 == b2:
    print('YES')
elif a1 == b1 and a2-1 == b2:
    print('YES')
elif a1-1 == b1 and a2+1 == b2:
    print('YES')
elif a1-1 == b1 and a2-1 == b2:
    print('YES')
elif a1+1 == b1 and a2-1 == b2:
    print('YES')
else:
    print('NO')
# шоколадка
n = int(input())
m = int(input())
k = int(input())
if n % 2 != 0 or m % 2 != 0:
    if k % 2 != 0:
        print('YES')
    else:
        print('NO')
elif n % 2 == 0 or m % 2 == 0:
    if k % 2 == 0:
        print('YES')
    else:
        print('NO')
# коровы
n = int(input())
s = n % 10
if 10 <= n <= 20 or s == 0 or 5 <= s <= 9:
    print(n, 'korov')
elif s == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
# знак числа
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)
# координатные четверти
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
    print('YES')
elif x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0:
    print('YES')
elif x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0:
    print('YES')
elif x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0:
    print('YES')
else:
    print('NO')
# сколько совпадает чисел
a, b, c = int(input()), int(input()), int(input())
if a == b and a == c:
    print(3)
elif b == c or a == c or a == b:
    print(2)
else:
    print(0)
# узник замка иф
a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if e < c and d < a:
    if a < e and d < c:
        if d < b and e < c:
            print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('YES')
# коробки
a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 == a2 and b1 == b2:
    print('Boxes are equal')
elif (a1 <= a2 and b1 <= b2) or (a1 <= b2 and b1 <= a2):
    print('The first box is smaller than the second one')
elif (a2 <= a1 and b2 <= b1) or (b2 <= a1 and a2 <= b1):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
# список квадратов
n = int(input())
i = 0
sqrt = i ** 2
while sqrt < n:
    sqrt = i ** 2
    if sqrt > n:
        break
    i = i + 1
    print(sqrt, end=' ')
# список квадратов
n = int(input())
i = 1
sqrt = i ** 2
while sqrt <= n:
    sqrt = i ** 2
    if sqrt > n:
        break
    i = i + 1
    print(sqrt, end=' ')
#
n = int(input())
i = 2
s = n % i
while s != 0:
    s = n % i
    i = i + 1
print(i-1)

####### 3 неделя
# площадь треуголника
import math

a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
if s % 1 == 0:
    print('{0:.0f}'.format(s))
elif s % 1 != 0:
    print('{0:.6f}'.format(s))
# сумма ряда
n = int(input())
i = 1
sym = 0
while i <= n:
    sym = sym + (1/(i**2))
    i = i + 1
if sym % 1 == 0:
    print('{0:.0f}'.format(sym))
elif sym % 1 != 0:
    print(float(sym))
# цена онлайн
n = float(input())
print(int(n // 1), round((n % 1) * 100))
# округление по российским правилам
import math

n = float(input())
s = math.floor((n % 1)*10)
if s >= 5:
    print(math.ceil(n))
elif s < 5:
    print(math.floor(n))
# проценты
import math

p, x, y = int(input()), int(input()), int(input())
sym = ((((x * 100) + y) * (100 + p)+10**(-9)) / 100) / 100
print(int(sym // 1), math.floor((sym % 1)*100))
# квадратное уравнение-1
import math

a, b, c = float(input()), float(input()), float(input())
d = (b ** 2 - 4 * (a * c))
if d > 0:
    n = (math.sqrt(d))
    x1 = (-b - n) / (2 * a)
    x2 = (-b + n) / (2 * a)
    if x1 % 1 == 0 and x1 % 1 == 0:
        if x1 > x2:
            print(int(x2), int(x1))
        elif x2 > x1:
            print(int(x1), int(x2))
    else:
        if x1 > x2:
            print(x2, x1)
        elif x2 > x1:
            print(x1, x2)
elif d == 0:
    x = (-b) / (2 * a)
    if x % 1 == 0:
        print(int(x))
    else:
        print(x)
