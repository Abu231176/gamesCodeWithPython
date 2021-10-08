def display_game(game_list):
    print("")
    print(game_list[6], game_list[7], game_list[8], sep="  |  ")
    print("=" * 13)
    print(game_list[3], game_list[4], game_list[5], sep="  |  ")
    print("=" * 13)
    print(game_list[0], game_list[1], game_list[2], sep="  |  ")
    print("")
# game_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# display_game(game_list)


def is_game_on(game_list):
    if game_list[0] == game_list[3] == game_list[6] == 'X' or game_list[0] == game_list[3] == game_list[6] == 'O':
        return False
    elif game_list[1] == game_list[4] == game_list[7] == 'X' or game_list[1] == game_list[4] == game_list[7] == 'O':
        return False
    elif game_list[2] == game_list[5] == game_list[8] == 'X' or game_list[2] == game_list[5] == game_list[8] == 'O':
        return False
    elif game_list[0] == game_list[1] == game_list[2] == 'X' or game_list[0] == game_list[1] == game_list[2] == 'O':
        return False
    elif game_list[3] == game_list[4] == game_list[5] == 'X' or game_list[3] == game_list[4] == game_list[5] == 'O':
        return False
    elif game_list[6] == game_list[7] == game_list[8] == 'X' or game_list[6] == game_list[7] == game_list[8] == 'O':
        return False
    elif game_list[0] == game_list[4] == game_list[8] == 'X' or game_list[0] == game_list[4] == game_list[8] == 'O':
        return False
    elif game_list[2] == game_list[4] == game_list[6] == 'X' or game_list[2] == game_list[4] == game_list[6] == 'O':
        return False
    elif game_list.count(' ') == 0:
        return False
    else:
        return True


def place_marker(game_list, position, marker):
    game_list[position - 1] = marker
    display_game(game_list)


def player_choice(game_list):
    position = "wrong"
    while position not in range(1, 10):
        position = input("Please enter next position of play (1-9) ")
        if position.isnumeric():
            position = int(position)
            if game_list[position - 1] != ' ':
                print("Sorry position is already filled")
        else:
            print("Sorry , Only numbers (1-9) are valid values ")

    return position


def player_input():
    marker = 'wrong'
    while marker not in ['X', 'O']:

        marker = input("Player1: Do you want to be X or O?  ")
        if marker not in ['X', 'O']:
            print("Sorry Invalid choice! ")
        else:
            print("Player1 will go first !!")
    return marker


def replay():

    choice = 'wrong'
    while choice not in ['Y', 'N']:

        choice = input("Do you want play again (Y/N): ")
        if choice not in ['Y', 'N']:
            print("Sorry Invalid choice! ")

    if choice == 'Y':
        return True
    else:
        return False


replay_on = True

while replay_on:

    game_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print("Welcome to Tic Tac Toe!")
    marker = player_input()

    game_on = True


    while game_on:

        position = player_choice(game_list)
        place_marker(game_list, position, marker)
        if marker == 'X':
            marker = 'O'
        else:
            marker = 'X'
        game_on = is_game_on(game_list)

    print("Game over!!")
    replay_on = replay()

print("Thank You playing Tic tac toe !!")