s=input()
i=input()
j=input()
def simmetr(s,i,j):
    return len(s) < 2 or s[i] == s[j] and simmetr(s[i-1:j])

def simmetr(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return simmetr(s[1:-1])