n = int(input())


def degree5(n):
    if n < 5 or n % 5 != 0:
        return -1
    return degree5()


print(degree5(n))
