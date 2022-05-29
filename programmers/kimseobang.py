def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "kim":
            break
    return "김서방은 " + str(i) + "에 있다"
