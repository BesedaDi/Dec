import math

a, b, c = float(input()), float(input()), float(input())
d = (b ** 2 - 4 * a * c)
print(d)
if d > 0:
    n = (math.sqrt(d))
    print(n)
    x1 = -b - n / 2*a
    x2 = -b + n / 2*a
    if x1 % 1 != 0 or x2 % 1 != 0:
        print(x1, x2)
    else:
        if x1 > x2:
            print(int(x2), math.floor(x1))
        elif x2 < x1:
            print(math.floor(x1), int(x2))
elif d == 0:
    x = -b / 2*a
    print(round(x))
