a=input()
n=input()
def maxlist(a):
    if a[-1]:
        return a[-1]
    return max(a[-1],maxlist(a-1))

print(maxlist(a,n))