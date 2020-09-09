
a1=int(input())
r=int(input())
n=int(input())

def progress(a1,r,n):
    if n == 1:
        return a1
    return a1+(n-1)*progress(a1, r, n-1)
print(progress(a1,r,n))