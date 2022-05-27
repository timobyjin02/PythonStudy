a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)

day = 1
while 1:
    day += 1
    if day % a == 0 and day % b == 0 and day % c == 0:
        break
print(day)
