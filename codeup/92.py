a, b, c = map(int, input().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:   # 만족할 때만 출력
    d += 1
print(d)
#=================================#
'''d = 1
while 1:    # while문 계속 반복 할 동안
    d += 1  # day도 1씩 증가
    if d%a == 0 and d%b == 0 and d%c == 0:  # a, b, c로 나누어서 0이 나오면 break
        break
print(d)'''
