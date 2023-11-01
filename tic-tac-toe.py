from time import sleep
from random import randint, choice
from secondary import check_o, check_x, give_column, give_line
from playsound import playsound
import winsound
names = ["Dark Vador", "Voldemort", "Joker", "Batman", "Iron-Man", "Vegeta", "Sangoku", "Harry Potter", "Venom", "The Penguin", "Orochimaru", "Naruto", "Sasuke"]
while True:
    class Cell:
        def __init__(self, value_of_cell, status_of_cell):
            # X or O or -
            self.value = value_of_cell
            # 2 full or 1 empty
            self.status = status_of_cell

    class Player:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    def print_game():
        """This function initialize the game and the list of lists and print the first state of the game"""
        list1 = [Cell(" - ", 1), Cell(" - ", 1), Cell(" - ", 1)]
        list2 = [Cell(" - ", 1), Cell(" - ", 1), Cell(" - ", 1)]
        list3 = [Cell(" - ", 1), Cell(" - ", 1), Cell(" - ", 1)]
        list_of_lists = [list1, list2, list3]
        printer(list_of_lists)
        return list_of_lists


    def player1(list_of_lists, lvl, player):
        """This function handle the player number 1"""
        print(first_player.name, "'s turn", sep="")
        choix = int(input("Choose the cell you want to play in: "))
        line = give_line(choix)
        column = give_column(choix)
        while (line != 0 and line != 1 and line != 2) or (column != 0 and column != 1 and column != 2):
            choix = int(input("Choose a valid cell you want to play in(1-9): "))
            line = give_line(choix)
            column = give_column(choix)
        while list_of_lists[line][column].status == 2:
            print("cell is full choose a new one.")
            choix = int(input("Choose the cell you want to play in: "))
            line = give_line(choix)
            column = give_column(choix)
            while (line != 0 and line != 1 and line != 2) or (column != 0 and column != 1 and column != 2):
                choix = int(input("Choose the cell you want to play in: "))
                line = give_line(choix)
                column = give_column(choix)
        list_of_lists[line][column].status = 2
        if player == "X":
            list_of_lists[line][column].value = " X "
        elif player == "O":
            list_of_lists[line][column].value = " O "
        printer(list_of_lists)
        if checker(list_of_lists) == 1:
            print(first_player.name, "win")
            playsound("audio/You_Win.wav")
            first_player.score += 1
            return
        elif checker(list_of_lists) == 2:
            print("It's a tie")
            return
        else:
            if lvl == 1 and player == "X":
                level_easy(list_of_lists, "O")
            elif lvl == 1 and player == "O":
                level_easy(list_of_lists, "X")
            elif lvl == 2 and player == "X":
                level_hard(list_of_lists, "O")
            elif lvl == 2 and player == "O":
                level_hard(list_of_lists, "X")
            elif lvl == 3 and player == "X":
                player2(list_of_lists, "O")
            elif lvl == 3 and player == "O":
                player2(list_of_lists, "X")


    def player2(list_of_lists, player):
        """This function handle the player number 2"""
        print(second_player.name, "'s turn", sep="")
        choix = int(input("Choose the cell you want to play in: "))
        line = give_line(choix)
        column = give_column(choix)
        while (line != 0 and line != 1 and line != 2) or (column != 0 and column != 1 and column != 2):
            choix = int(input("Choose a valid cell you want to play in (1-9): "))
            line = give_line(choix)
            column = give_column(choix)
        while list_of_lists[line][column].status == 2:
            print("cell is full choose a new one.")
            choix = int(input("Choose the cell you want to play in: "))
            line = give_line(choix)
            column = give_column(choix)
            while (line != 0 and line != 1 and line != 2) or (column != 0 and column != 1 and column != 2):
                choix = int(input("Choose the cell you want to play in: "))
                line = give_line(choix)
                column = give_column(choix)
        list_of_lists[line][column].status = 2
        if player == "X":
            list_of_lists[line][column].value = " X "
        elif player == "O":
            list_of_lists[line][column].value = " O "
        print("Player 2 played in:", choix)
        printer(list_of_lists)
        if checker(list_of_lists) == 1:
            print(second_player.name, "win")
            second_player.score += 1
            playsound("audio/You_Win.wav")
            return
        elif checker(list_of_lists) == 2:
            print("It's a tie")
            return
        else:
            if player == "O":
                player1(list_of_lists, 3, "X")
            elif player == "X":
                player1(list_of_lists, 3, "O")


    def level_easy(list_of_lists, player):
        """This function handle the easy bot"""
        print(second_player.name, "'s turn", sep="")
        sleep(2)
        choix = randint(1, 9)
        line = give_line(choix)
        column = give_column(choix)
        while list_of_lists[line][column].status == 2:
            choix = randint(1, 9)
            line = give_line(choix)
            column = give_column(choix)
        list_of_lists[line][column].status = 2
        if player == "X":
            list_of_lists[line][column].value = " X "
        elif player == "O":
            list_of_lists[line][column].value = " O "
        print(second_player.name, "played in:", choix)
        printer(list_of_lists)
        if checker(list_of_lists) == 1:
            print(second_player.name, "win")
            playsound("audio/You_Lose.wav")
            second_player.score += 1
            return
        elif checker(list_of_lists) == 2:
            print("It's a tie")
            return
        else:
            if player == "O":
                player1(list_of_lists, 1, "X")
            elif player == "X":
                player1(list_of_lists, 1, "O")

    def level_hard(list_of_lists, player):
        """This function handle the hard bot"""
        print(second_player.name, "'s turn", sep="")
        sleep(2)
        choix = check_o(list_of_lists)
        if choix == 404:
            choix = check_x(list_of_lists)
        if choix == 405:
            choix = randint(1, 9)
        line = give_line(choix)
        column = give_column(choix)
        while list_of_lists[line][column].status == 2:
            choix = randint(1, 9)
            line = give_line(choix)
            column = give_column(choix)
        list_of_lists[line][column].status = 2
        if player == "X":
            list_of_lists[line][column].value = " X "
        elif player == "O":
            list_of_lists[line][column].value = " O "
        print("Player 2 played in:", choix)
        printer(list_of_lists)
        if checker(list_of_lists) == 1:
            print(second_player.name, "win")
            playsound("audio/You_Lose.wav")
            second_player.score += 1
            return
        elif checker(list_of_lists) == 2:
            print("It's a tie")
            return
        else:
            if player == "O":
                player1(list_of_lists, 2, "X")
            elif player == "X":
                player1(list_of_lists, 2, "O")


    def printer(list_of_lists):
        """"This function print all changes made during the game"""
        print("\n\n\n")
        for n in range(len(list_of_lists)):
            print("\t\t\t\t\t\t\t\t\t\t", end="")
            for i in range(len(list_of_lists[n])):
                print("||", list_of_lists[n][i].value, end="", sep="")
            print("||", end="")
            print("\t", n+1+(n*2), n+2+(n*2), n+3+(n*2), sep=" | ", end=" |\n")


    def checker(list_of_lists):  # Will be used to check the status of the game for both pvp and vs IA
        """"This function checks if the game is finished (one of the player won or a tie)"""
        cnt = 0  # Used to check if tie
        for n in range(3):
            if list_of_lists[n][0].value == list_of_lists[n][1].value == list_of_lists[n][2].value and list_of_lists[n][0].status == 2:
                return 1  # The function that gets the return its player has won
        for i in range(0, 3):
            if list_of_lists[0][i].value == list_of_lists[1][i].value == list_of_lists[2][i].value and list_of_lists[0][i].status == 2:
                return 1  # The function that gets the return its player has won
        # Case diagonal win (1)
        if list_of_lists[0][0].value == list_of_lists[1][1].value == list_of_lists[2][2].value and list_of_lists[0][0].status == 2:
            return 1
        if list_of_lists[0][2].value == list_of_lists[1][1].value == list_of_lists[2][0].value and list_of_lists[2][0].status == 2:
            return 1
        for i in range(3):
            for b in range(3):
                if list_of_lists[i][b].status == 2:
                    cnt += 1
        if cnt == 9:
            return 2
        # Continue (0)


    def print_menu():
        """"This function print the menu"""
        print("\t\t\t\t\t\t\t\t\t\t----------- Welcome to TIC TAC TOE -----------\n\n\n")
        print("1)Easy\n2)Hard\n3)PVP")
        levels = int(input("Choose a level (1/2/3): "))
        while levels < 1 or levels > 4:
            print("1)Easy\n2)Hard\n3)PVP")
            print("Please enter a valid number.")
            levels = int(input("Choose a level (1/2/3): "))
        return levels

    try:
        answer = "z"
        counting = "NOT SAME"
        while answer != "N":
            s1 = 0
            s2 = 0
            answer = "z"
            level = print_menu()
            if counting == "NOT SAME":
                p1 = input("Enter your name: ")
                p1 = p1.capitalize()
                p2 = input("Enter your opponent's name (type random for a random name): ")
                p2 = p2.capitalize()
                if p2 == "Random":
                    p2 = choice(names)
                first_player = Player(p1, s1)
                second_player = Player(p2, s2)
            counting = "SAME"
            symbol = input("With what symbol do you want to play: (X/O) ")
            symbol = symbol.upper()
            while symbol != "X" and symbol != "O":
                symbol = input("With what symbol do you want to play: (X/O) ")
                symbol = symbol.upper()
            if symbol == "X":
                player1(print_game(), level, "X")
            elif symbol == "O" and level == 1:
                level_easy(print_game(), "X")
            elif symbol == "O" and level == 2:
                level_hard(print_game(), "X")
            elif symbol == "O" and level == 3:
                player2(print_game(), "X")
            print("\t\t\t\t\t\t\t\t\t\t------", first_player.name, "((((", first_player.score, "---", second_player.score, "))))", second_player.name, "------")
            while answer != "Y" and answer != "N":
                print()
                answer = input("Do you want to play again: (Y/N) ")
                answer = answer.upper()
                print("\n\n")
            if answer == "Y":
                counting = input("Are the same players playing next round or do you want to enter new players (The score will be reset): (same/not same)")
                counting = counting.upper()
                while counting != "SAME" and counting != "NOT SAME":
                    counting = input("Are the same players playing next round or do you want to enter new players (The score will be reset): (same/not same)")
                    counting = counting.upper()
    except:
        print("You entered a wrong value the game will restart.")
        sleep(2)
        for q in range(3, 0, -1):
            print("The game will restart in: ", q)
            sleep(1)
            winsound.Beep(1500, 500)
    else:
        exit()
