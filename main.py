#-------Global variables-------#

#game board
board = ["-", "-", "-",      #list containing 9 elements 
         "-" ,"-", "-", 
         "-", "-", "-"]

#if game is still going
game_still_going = True 

#who won? or tie?
winner = None

#whose turn is it?
current_player = "X"


def display_board():         #function to display the board
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():              #function to play the game 
  
  #display initial board
  display_board()             #calling the display_board function

  #while the game is still going
  while game_still_going:

    #handle a single turn of an arbitrary player
    handle_turn(current_player)

    #check id the game has ended
    check_if_game_over()

    #flipping to the other player
    flip_player()

  #the game has ended
  if winner == "X" or winner == "0":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


#handle a single turn of an arbitrary player
def handle_turn(player):
  print (player + "'s turn.")
  position = input("Choose a position from 1-9: ")   #takes input from user and stores it into position 

  valid = False 
  while not valid:
    
    #make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
    
    position = int(position) - 1    #converts string to integer and stores it into position

    #make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print ("You can't go there. Go again.")
    
  

  board[position] = player           #assigns X to position on within the board  
  display_board()                 #displaying the board after the change


def check_if_game_over():
  check_for_winner()
  check_if_tie()



def check_for_winner():

  #set up global variables
  global winner 
  
  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    #there was no win
    winner = None
  return                         #ends function

def check_rows():
  #Set up global variables 
  global game_still_going
  #check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False 
  #determines which playes is the winner  
  if row_1:
    return board[0]               #returns the value in board[0] (X or 0) to check_rows
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  #Set up global variables 
  global game_still_going
  #check if any of the rows have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False 
  #determines which playes is the winner  
  if column_1:
    return board[0]               #returns the value in board[0] (X or 0) to check_rows
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  #Set up global variables 
  global game_still_going
  #check if any of the rows have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  #if any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False 
  #determines which playes is the winner  
  if diagonal_1:
    return board[0]               #returns the value in board[0] (X or 0) to check_rows
  elif diagonal_2:
    return board[6]
  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  #global variables we need
  global current_player
  #if the current player was X, then change it to O
  if current_player == "X":
    current_player = "0"
  #if the current player was O, then change it to X
  elif current_player == "0":
    current_player = "X"
  return
  

play_game()
