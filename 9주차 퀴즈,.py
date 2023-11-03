height = int(input("크리스마스 트리의 높이를 설정하세요: "))

for i in range(1, height + 1):
    spaces = height - i
    stars = 2 * i - 1

    for j in range(spaces):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")

    print()
