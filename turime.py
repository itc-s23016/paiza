def f(p):
    return a + 10 if a >= 10 else a


p = int(input())
a = p // 100
result = f(p)
print(result)
