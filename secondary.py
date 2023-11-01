def check_o(list_of_lists):
    for n in range(3):
        if list_of_lists[0][n].value == list_of_lists[1][n].value == " O " and list_of_lists[2][n].status == 1:
            if n == 0:
                return 7
            elif n == 1:
                return 8
            elif n == 2:
                return 9
        elif list_of_lists[2][n].value == list_of_lists[1][n].value == " O " and list_of_lists[0][n].status == 1:
            if n == 0:
                return 1
            elif n == 1:
                return 2
            elif n == 2:
                return 3
        elif list_of_lists[0][n].value == list_of_lists[2][n].value == " O " and list_of_lists[1][n].status == 1:
            if n == 0:
                return 4
            elif n == 1:
                return 5
            elif n == 2:
                return 6
        elif list_of_lists[n][0].value == list_of_lists[n][1].value == " O " and list_of_lists[n][2].status == 1:
            if n == 0:
                return 3
            elif n == 1:
                return 6
            elif n == 2:
                return 9
        elif list_of_lists[n][0].value == list_of_lists[n][2].value == " O " and list_of_lists[n][1].status == 1:
            if n == 0:
                return 2
            elif n == 1:
                return 5
            elif n == 2:
                return 8
        elif list_of_lists[n][2].value == list_of_lists[n][1].value == " O " and list_of_lists[n][0].status == 1:
            if n == 0:
                return 1
            elif n == 1:
                return 4
            elif n == 2:
                return 7
        elif list_of_lists[0][0].value == list_of_lists[1][1].value == " O " and list_of_lists[2][2].status == 1:
            return 9
        elif list_of_lists[2][2].value == list_of_lists[1][1].value == " O " and list_of_lists[0][0].status == 1:
            return 1
        elif list_of_lists[0][0].value == list_of_lists[2][2].value == " O " and list_of_lists[1][1].status == 1:
            return 5
        elif list_of_lists[0][2].value == list_of_lists[1][1].value == " O " and list_of_lists[2][0].status == 1:
            return 7
        elif list_of_lists[2][0].value == list_of_lists[1][1].value == " O " and list_of_lists[0][2].status == 1:
            return 3
        elif list_of_lists[0][2].value == list_of_lists[2][0].value == " O " and list_of_lists[1][1].status == 1:
            return 5
    return 404


def check_x(list_of_lists):
    for n in range(3):
        if list_of_lists[0][n].value == list_of_lists[1][n].value == " X " and list_of_lists[2][n].status == 1:
            if n == 0:
                return 7
            elif n == 1:
                return 8
            elif n == 2:
                return 9
        elif list_of_lists[2][n].value == list_of_lists[1][n].value == " X " and list_of_lists[0][n].status == 1:
            if n == 0:
                return 1
            elif n == 1:
                return 2
            elif n == 2:
                return 3
        elif list_of_lists[0][n].value == list_of_lists[2][n].value == " X " and list_of_lists[1][n].status == 1:
            if n == 0:
                return 4
            elif n == 1:
                return 5
            elif n == 2:
                return 6
        elif list_of_lists[n][0].value == list_of_lists[n][1].value == " X " and list_of_lists[n][2].status == 1:
            if n == 0:
                return 3
            elif n == 1:
                return 6
            elif n == 2:
                return 9
        elif list_of_lists[n][0].value == list_of_lists[n][2].value == " X " and list_of_lists[n][1].status == 1:
            if n == 0:
                return 2
            elif n == 1:
                return 5
            elif n == 2:
                return 8
        elif list_of_lists[n][2].value == list_of_lists[n][1].value == " X " and list_of_lists[n][0].status == 1:
            if n == 0:
                return 1
            elif n == 1:
                return 4
            elif n == 2:
                return 7
        elif list_of_lists[0][0].value == list_of_lists[1][1].value == " X " and list_of_lists[2][2].status == 1:
            return 9
        elif list_of_lists[2][2].value == list_of_lists[1][1].value == " X " and list_of_lists[0][0].status == 1:
            return 1
        elif list_of_lists[0][0].value == list_of_lists[2][2].value == " X " and list_of_lists[1][1].status == 1:
            return 5
        elif list_of_lists[0][2].value == list_of_lists[1][1].value == " X " and list_of_lists[2][0].status == 1:
            return 7
        elif list_of_lists[2][0].value == list_of_lists[1][1].value == " X " and list_of_lists[0][2].status == 1:
            return 3
        elif list_of_lists[0][2].value == list_of_lists[2][0].value == " X " and list_of_lists[1][1].status == 1:
            return 5
    return 405


def give_line(line):
    if line == 1 or line == 2 or line == 3:
        return 0
    elif line == 4 or line == 5 or line == 6:
        return 1
    elif line == 7 or line == 8 or line == 9:
        return 2
    else:
        return 3


def give_column(column):
    if column == 1 or column == 4 or column == 7:
        return 0
    elif column == 2 or column == 5 or column == 8:
        return 1
    elif column == 3 or column == 6 or column == 9:
        return 2
    else:
        return 3
