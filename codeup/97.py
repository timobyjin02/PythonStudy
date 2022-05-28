# 1. 초기 십자 바둑판 입력
baduk = []
for _ in range(19):
    matrix = list(map(int, input().split()))
    baduk.append(matrix)
    n = int(input())
# 2. n과 자표 값을 입력 받고 그에 따라 십자 형태에 맞춰 흑 -> 백, 백 -> 흑으로 변환
for i in range(n):
    x, y = map(lambda num: int(num)-1, input().split())
    for i in range(19):
        baduk[i][x] = 1 if baduk[i][x] == 0 else 0  # x가 0이면 1로 바꿔주고, 아니면 0
        baduk[i][y] = 1 if baduk[i][y] == 0 else 0

# 3. 변환된 값을 한 줄 단위로 출력
for i in range(19):
    print(*baduk[i])
