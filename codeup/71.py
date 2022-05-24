def goto(array, i):
    if array[i] == 0:
        return
    print(array[i])
    i += 1
    goto(array, i)

    array = list(map(int, input().split()))
    goto(array, i=0)
