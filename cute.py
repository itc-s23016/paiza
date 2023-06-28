def f(n, m):
    return "ok" if m % n == 0 else "ng"


[n, m] = [int(_) for _ in input().split()]
result = f(n, m)
print(result)
