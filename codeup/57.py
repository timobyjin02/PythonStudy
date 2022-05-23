for i in range(4):
    a, b = map(int(input().split()))
    print((not a) and (not b) or (a and b))
