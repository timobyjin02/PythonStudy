ant_house = []
for i in range(5):
    m = list(map(int, input().split()))
    ant_house.append(m)

x, y = 1, 1
# 자기 자신의 좌표(먹이)가 찾기 전까지 움짐임
while ant_house[x][y] != 2:
    if ant_house[x][y] == 0:    # 본인 자리가 0이면
        ant_house[x][y] = 9    # 9로 바꿔준다
        y += 1
    else:
        x += 1
        y -= 1
ant_house[x][y] = 9

for i in ant_house:
    print(*i)
