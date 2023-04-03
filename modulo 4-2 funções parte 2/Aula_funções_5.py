
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


print(somar(3, 2, 5))
print(somar(8, 4))
print(somar())
r1  = somar(10, 10, 10)
r2 = somar(100, 1000, 10000)
print(f'Result = {r1} e {r2}')
