integer = input()
count = len(integer)-1
for i in range(len(integer)):
    print([int(integer[i] + '0'*count)])
    count -= 1
