a1=int(input())
r=int(input())
n=int(input())
def sum_progress(a1, r, n):
    if n == 1:
        return a1
    return a1 + a1 + (n - 1) * sum_progress(a1, r, n - 1)
print(sum_progress(a1,r,n))