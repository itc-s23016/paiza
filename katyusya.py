def f(n, p, m, q):
    return a + b


[[n, p], [m, q]] = [map(int, input().split()) for _ in range(2)]
a = n * p
b = q * ((n + (m - 1)) // m)
result = f(n, p, m, q)
print(result)
