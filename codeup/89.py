a, d, n = map(int, input().split())
i = a
arith = []
while len(arith) < n:
    arith.append(i)
    i += d
print(arith[-1])
