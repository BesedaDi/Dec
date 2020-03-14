def BinSearch_iter(lst, x):
    start = 0
    end = len(lst)
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

def iter():
    import random
    import timeit

    lst = []
    for _ in range(1000):
        a = random.randint(0, 10000)
        lst.append(a)
    lst.sort()
    print(*lst)
    x = int(input())
    print(BinSearch_iter(lst, x))
    print(timeit.timeit())
iter()