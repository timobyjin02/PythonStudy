a, b, c = map(int, input().split())
print('odd' if a % 2 else 'even')
print(b % 2 and 'odd' or 'even')
print(['even', 'odd'][c % 2])
