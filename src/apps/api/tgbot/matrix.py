def matrix(n):
    list = [[0 for j in range(n)] for i in range(n)]

    sdvig = 0
    side = n
    number = 1

    while sdvig < (n / 2):
        for j in range(sdvig, side):
            list[sdvig][j] = number
            number += 1
        for i in range(sdvig + 1, side - 1):
            list[i][side - 1] = number
            number += 1
        for j in range(side - 1, sdvig - 1, -1):
            list[side - 1][j] = number
            number += 1
        for i in range(side - 2, sdvig, -1):
            list[i][sdvig] = number
            number += 1
        side -= 1
        sdvig += 1

    if n % 2 == 1:
        list[n // 2][n // 2] = n ** 2

    s = beautiful_print(list)

    return s


def beautiful_print(list):
    join_rows = []
    for row in list:
        join_rows.append(' '.join(str(num) for num in row))
    join_lines = "\n".join(line for line in join_rows)
    return join_lines
