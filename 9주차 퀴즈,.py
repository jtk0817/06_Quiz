# 크리스마스 트리의 높이를 사용자에게 입력받음
height = int(input("크리스마스 트리의 높이를 설정하세요: "))

# 크리스마스 트리 출력
for i in range(1, height + 1):
    # 공백의 개수 계산
    spaces = height - i
    # 별의 개수 계산
    stars = 2 * i - 1

    # 공백 출력
    for j in range(spaces):
        print(" ", end="")

    # 별 출력
    for j in range(stars):
        print("*", end="")

    # 줄바꿈
    print()
