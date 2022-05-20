from re import M


y, m, d = input().split('.')
if len(m) == 1:
    m = '0' + m
if len(d) == 1:
    d = '0' + d
print('{},{},{}'.format(y, m, d))
