h, w = map(int, input().split())
shape = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x-1, y-1

    if d == 0:
        for i in range(1):
            shape[x][y + i] = 1  # d가 0이면 y는 가로로 바꿔줘야 하기 때문에 +1씩 해준다
    else:
        for i in range(1):
            shape[x + 1][y] = 1

for s in shape:
    print(*s)
