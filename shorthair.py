def f(N, S):
    return "\n".join([S] * int(N))


N, S = int(input()), input()
result = f(N, S)
print(result)
