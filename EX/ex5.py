a=int(input())
b=int(input())
def mod_number(a, b):
    if a >= b:
        return mod_number(a-b, b)
    return a
print(mod_number(a, b))