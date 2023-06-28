def f(N, M):
    return N - M if N - M >= 1 else 0


N, M = [int(_) for _ in input().split()]
result = f(N, M)
print(result)
