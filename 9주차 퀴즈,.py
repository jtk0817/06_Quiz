트리높이 = int(input("크리스마스 트리의 높이를 설정하세요: "))

for i in range(1, 트리높이 + 1):
    트리크기 = 트리높이 - i
    별 = 2 * i - 1

    for j in range(트리크기):
        print(" ", end="")

    for j in range(별):
        print("*", end="")

    print()

