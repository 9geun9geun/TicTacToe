#---Global variables---
board = ["-","-","-",  #GAMEBOARDd
         "-","-","-",
         "-","-","-"]
game_still_going = True   #If game still going
winner = None             #result, who won?
current_player = "X"      #current player



def display_board():
  print(board[0]+ " | " + board[1] + " | " + board[2])
  print(board[3]+ " | " + board[4] + " | " + board[5])
  print(board[6]+ " | " + board[7] + " | " + board[8])


def play_game():        #play tictactoe1
  display_board()       #display the inital board

  while game_still_going:
    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  if winner == "X" or winner =="O":
    print(winner + " won!")
  elif winner == None:
    print("Tie!")
  

def handle_turn(player):
  print()
  print(player +"'s turn")
  position = input("Enter a position from 1-9: ")
  
  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid. Choose a position from 1-9: ")
      print(position)
    position = int(position) -1 
    if board[position] == "-":
      valid = True
    else:
      print("You cannot place there. Try again: ") 
  
  board[position] = player
  display_board()



def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  global winner
  row_winner = check_rows()             #checkrow
  column_winner = check_columns()       #checkcolumn
  diagonal_winner = check_diagonals()   #checkdiagonal
  
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  global game_still_going       #global variables
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  if row1 or row2 or row3:      #if there is a win
    game_still_going = False    #game stops
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return


def check_columns():
  global game_still_going       #global variables
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"
  if column1 or column2 or column3:      #if there is a win
    game_still_going = False    #game stops
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  return
  


def check_diagonals():
  global game_still_going       #global variables
  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"
  
  if diagonal1 or diagonal2:      #if there is a win
    game_still_going = False      #game stops
  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[2]
  return
  


def check_if_tie():
  global game_still_going
  
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  global current_player         #global variable
  if current_player == "X":     #if current player = X then change to O
    current_player = "O"
  elif current_player == "O":   #if current player = O then change to X
    current_player = "X"
  return 


play_game()
