k=input()
def half_digit(k):
    s=len(k)
    if s%2==0:
        s1 = s / 2
        s2=len(k)+1
        a = k[0:round(s1)]
        b = k[round(s1):round(s2)]
        a1=list(a)
        b1=list(b)
        a1 = [int(a) for a in a1]
        b1 = [int(b) for b in b1]
        n1=sum(a1)
        n2=sum(b1)
        if n1<n2:
            k1 = b + a
            print(k1)
        else:
            print(k)
    else:
        s1 = s / 2
        s3=s1+1
        s2 = len(k) + 1
        a = k[0:int(s1)]
        b = k[int(s3):int(s2)]
        a1 = list(a)
        b1 = list(b)
        a1 = [int(a) for a in a1]
        b1 = [int(b) for b in b1]
        print(a1)
        print(b1)
        n1 = sum(a1)
        n2 = sum(b1)
        if n1 < n2:
            k3=k[int(s1)]
            k1 = b+k3+a
            print(k1)
        else:
            print(k)
half_digit(k)
