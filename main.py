board_positions={}
for x in range(9):
    board_positions[x]='V'
acceptable_moves={'x','X','o','O'}
print("Welcome to Tic_tac Toe! In this game, player 1 will be X and player 2 will be O.\nOn the board, a 'V' represents a Vacant slot.\n")

print("When selecting the position, use the numbers shown below as a reference. \n")

def print_board(board_positions):
    print(board_positions[0] + " | " + board_positions[1] + " | " + board_positions[2])
    print(board_positions[3] + " | " +board_positions[4] + " | " +board_positions[5])
    print(board_positions[6] + " | " +board_positions[7] + " | " + board_positions[8])

def print_sample_board():
    print("0" + " | " + "1" + " | " + "2")
    print('3' + " | " + '4' + " | " + '5')
    print('6' + " | " + '7' + " | " + '8')

def game_over(board_positions):
    game_over=True

    for x,y in board_positions.items():
        if y=='V':
            game_over=False
    return game_over

def check_valid(attempted_location,board_positions,acceptable_moves):
    if board_positions[attempted_location] in acceptable_moves:
        return False
    else:
        return True
def check_if_won(board_positions,move):
    won=False
    if (board_positions[0]==move and board_positions[1]==move and board_positions[2]==move):
        won=True
    if (board_positions[3]==move and board_positions[4]==move and board_positions[5]==move):
        won=True
    if (board_positions[6]==move and board_positions[7]==move and board_positions[8]==move):
        won=True
    if (board_positions[0]==move and board_positions[3]==move and board_positions[6]==move):
        won=True
    if (board_positions[1]==move and board_positions[4]==move and board_positions[7]==move):
        won=True
    if (board_positions[2]==move and board_positions[5]==move and board_positions[8]==move):
        won=True
    if (board_positions[0]==move and board_positions[4]==move and board_positions[8]==move):
        won=True
    if (board_positions[2]==move and board_positions[4]==move and board_positions[6]==move):
        won=True
    return won
def turns(board_positions,acceptable_moves):
    while True:
        move = "x"
        while True:
            print("Player 1, enter your desired location: ")
            location = input()
            try:
                location = int(location)
            except:
                print("You must enter an integer. ")
                continue
            if location<0 or location>=9:
                print("You must enter a value between 0 and 8 ('Inclusive')")
                continue
            if not check_valid(location, board_positions, acceptable_moves):
                print("That position is already played. Please enter a free position: ")
                continue
            board_positions[location] = move
            print_board(board_positions)
            if check_if_won(board_positions,move):
                print("Player 1 wins!!!!\n\n")

            if game_over(board_positions) and not check_if_won(board_positions,move):
                print("Game over. Tie. ")
                break
            break
        break
    while True:
        move = "o"
        while True:
            print("Player 2, enter your desired location: ")
            location = input()
            try:
                location = int(location)
            except:
                print("You must enter an integer. ")
                continue
            if location < 0 or location >= 9:
                print("You must enter a value between 0 and 8 ('Inclusive')")
                continue
            if not check_valid(location, board_positions, acceptable_moves):
                print("That position is already played. Please enter a free position: ")
                continue
            board_positions[location] = move
            print_board(board_positions)
            if check_if_won(board_positions,move):
                print("Player 2 wins!!!!\n\n")
            if game_over(board_positions) and not check_if_won(board_positions,move):
                print("Game over. Tie. ")
                break
            break
        break

print_sample_board()
while True:

    turns(board_positions,acceptable_moves)


