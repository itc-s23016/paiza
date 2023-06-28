def f(n, m):
    return b if m % a == 0 else b + 1


[n, m] = [int(input()) for _ in range(2)]
a = n * 2
b = m // a
result = f(n, m)
print(result)
