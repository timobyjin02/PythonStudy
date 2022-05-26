r, g, b = map(int, input().split())
res = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j, k)
            res += 1
print(res)