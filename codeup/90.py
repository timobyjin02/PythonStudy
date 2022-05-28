from typing import Mapping


a, r, n = map(int, input().split())

i = a
count = 0
geom = []
while count < 0:
    geom.append(i)
    i += r
    count += 1
    print(geom[-1])
