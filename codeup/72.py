n = int(input())
num = list(map(int, input().split()))
num.reverse()


def goto(num, n):
    print(num[n])
    n -= 1
    if n == -1:
        return
    goto(num, n)


goto(num, n-1)
