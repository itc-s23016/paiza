def f(n, m, ts):
    return "OK" if c == m else c


[n, m] = [int(input()) for _ in range(2)]
ts = [int(input()) for _ in range(m)]
t = n * 60
c = 0
for i in ts:
    if i < t:
        t -= i
        c += 1
    else:
        break
result = f(n, m, ts)
print(result)
