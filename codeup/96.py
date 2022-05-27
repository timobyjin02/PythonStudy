import numpy as np
n = int(input())
baduk = np.zeros((19, 19), dtype=int)
# baduk = [[0 for _ in range(19)] for _ in rnage(19)]

for _ in range(n):
    x, y = map(int, input().split())
    baduk[x-1][y-1] = 1

for bd in baduk:
    print(*bd)
