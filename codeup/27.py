y, m, d = input().split('.')
m = '0'+m if len(m) == 1 else m
d = '0'+d if len(d) == 1 else d
print('{}-{}-{}'.format(d, m, y))
