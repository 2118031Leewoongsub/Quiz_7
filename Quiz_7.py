christmas_tree_height = int(input("크리스마스 트리의 높이를 입력하세요.: "))
for i in range(christmas_tree_height):
    for x in range(christmas_tree_height - i - 1):
        print(" ", end="")
    for y in range(i * 2 +1):
        print("*", end="")
    print()
