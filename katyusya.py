[[n, p], [m, q]] = [map(int, input().split()) for _ in range(2)]
a = n * p
b = q * ((n + (m - 1)) // m)
print(a + b)
