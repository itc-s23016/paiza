[n, m] = [int(input()) for _ in range(2)]
a = n * 2
b = m // a
if m % a == 0:
    print(b)
else:
    print(b + 1)
