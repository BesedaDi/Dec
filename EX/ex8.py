k = input()


def fib(k):
    if k in (1, 2):
        return 1
    return fib(k - 1) + fib(k - 2)


print(fib(k))
