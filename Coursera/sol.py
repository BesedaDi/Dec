import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
y = (f - c * e) / (d - c * b)
x = (e - b * y) / a
if x % 1 == 0 and y % 1 == 0:
    print(int(x), int(y))
else:
    if x > y:
        print(math.ceil(x), math.ceil(y))
    else:
        print(math.ceil(y), math.ceil(x))
