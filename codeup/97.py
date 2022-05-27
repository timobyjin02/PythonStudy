# 1. 초기 십자 바둑판 입력
baduk = []
for _ in range(19):
    matrix = list(map(int, input().split()))
    baduk.append(matrix)

# 2. n과 좌표 값을 입력받고 그에 따라 십자 형태에 맞춰 흑->백, 백->흑으로 변환
n = int(input())
for _ in range(n):  # n번 입력
    x, y = map(int, input().split())  # x와 y 좌표 입력
    for i in range(19):  # 변환
        baduk[i][y-1] = 1 if baduk[i][y-1] == 0 else 0  # 0->1, 1->0으로 변환
        baduk[x-1][i] = 1 if baduk[x-1][i] == 0 else 0  # 0->1, 1->0으로 변환

# 3. 변환된 값을 한 줄 단위로 출력
for i in range(19):
    print(*baduk[i])
