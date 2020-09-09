n = int(input())
k = int(input())


def combin(n, k):
    return combin(n - 1, k) * n / (combin(n, k - 1) * combin(n - k - 1, n - k - 1))


print(combin(n, k))
