num = int(input())

print('== #1 정답 ==')
#1
for i in range(1, num+1):
  count = i if i%3 else 'X'
  print(count, end=' ')

print('\n== #2 오답 ==')
#2
for i in range(1, num+1):
  count = 'X' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i
  print(count, end=' ')