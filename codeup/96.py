
n = int(input())
baduk = [[0 for _ in range(19)] for _ in range(19)]

for _ in range(n):
    x, y = map(int, input().split())
    baduk[x-1][y-1] = 1   # 0, 0 부터 시작하기 때문에 -1 해준다, 그리고 들어올때마다 해당 좌표를 1로 해준다

for i in baduk:
    print(*i)
