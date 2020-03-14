def BinSearch_rec(lst, x, start=0, end=None):
    if end is None:
        end = len(lst)
    if start > end:
        return None
    m = (start + end) // 2
    if x == lst[m]:
        return m
    if x < lst[m]:
        return BinSearch_rec(lst, x, start, m - 1)
    # x > lst[m]
    return BinSearch_rec(lst, x, m + 1, end)




def rec():
    import random
    import timeit

    lst = []
    for _ in range(1000):
        a = random.randint(0, 10000)
        lst.append(a)
    lst.sort()
    print(*lst)
    x = int(input())
    print(BinSearch_rec(lst, x, start=0, end=None))
    print(timeit.timeit())

rec()

