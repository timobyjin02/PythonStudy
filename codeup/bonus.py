cur = tuple(map(int, input().split()))
lf, rgt, up, down = map(int, input().split())
coords = [[0 for _ in range(5)] for _ in range(5)]

move = (cur[0] - up + down, cur[1] - lf + rgt)
coords[move[0] - 1][move[1] - 1] = 1

for crd in coords:
    print(*crd)
