n = int(input())
num = int(input().split())
student = [0 for _ in range(23)]  # 0 ~ 22번까지 0으로 채워준
for i in num:
    student[i-1] += 1
print(*student)
