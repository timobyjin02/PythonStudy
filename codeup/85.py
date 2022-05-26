h, b, c, s = map(int, input().split())
gop = h * b * c * s
res = gop / (8 * 1024 * 1024)
print(round(res, 1), 'MB')
