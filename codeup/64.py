a, b, c = map(int, input().split())
n = a if a < b else b
print(n if n < c else c)