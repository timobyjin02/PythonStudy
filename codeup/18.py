from re import M
a, b, c = input().split('.')
if len(b) == 1:
    b = '0' + b
if len(c) == 1:
    c = '0' + c
print('{},{},{}'.format(a, b, c))
