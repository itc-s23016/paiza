def f(N, alist):
    return b[c - 1]


N = int(input())
alist = map(int, input().split()[:N])
b = [a for a in alist]
b.sort()
c = (N + 1) // 2
result = f(N, alist)
print(result)
