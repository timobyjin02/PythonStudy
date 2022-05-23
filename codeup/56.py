for i in range(4):
    a, b = map(int, input().split())
    print((a and (not b)) or ((not a) and b))
