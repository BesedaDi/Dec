##########
def BinSearch_rec(lst, x, start=0, end=None):
    if end == None:
        end = len(lst) - 1
    if start > end:
        return None

    m = (start + end) // 2
    if x == lst[m]:
        return m
    if x < lst[m]:
        return BinSearch_rec(lst, x, start, m - 1)
    # x > lst[m]
    return BinSearch_rec(lst, x, m + 1, end)


def BinSearch_iter(lst, x):
    start = 0
    end = len(lst) - 1
    m = end // 2
    while lst[m] != x and start < end:
        if x > lst[m]:
            start = m + 1
        else:
            end = m - 1
        m = (start + end) // 2
    if start > end:
        return None
    else:
        return m


def rec(lst, x):
    import timeit

    print(BinSearch_rec(lst, x, start=0, end=None))
    print(timeit.timeit())


def iter(lst, x):
    import timeit
    print(BinSearch_iter(lst, x))
    print(timeit.timeit())


def main():
    import random

    lst = []
    for _ in range(1000):
        a = random.randint(0, 1000)
        lst.append(a)
    lst.sort()
    print(*lst)
    x = int(input())
    rec(lst, x)
    iter(lst, x)


main()
