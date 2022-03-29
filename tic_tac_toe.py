
space_num=20
board='_'*space_num

def player_mv():
    '''return player move and marked on board'''
    global board
    player_mv=int(input('1-20 choose one number'))
    while player_mv>space_num or player_mv<1 or board[player_mv-1]!='_':
        if player_mv>space_num or player_mv<1:
          print('you must choose within 1-',space_num)
          player_mv=int(input('1-20 choose one number'))
        if board[player_mv-1]!='_':
          print('This space has been occupied, please choose other number')
          player_mv=int(input('1-20 choose one number'))
    if board[player_mv-1]=='_':
      board=board[:player_mv-1]+board[player_mv-1].replace('_','X')+board[player_mv:]
    else:
      print('be good ok?')
    return board
def display_board():
    '''print current board with pc and play moves'''
    print(board)

def start_game():
    '''initial a game'''
    print("Let's start a game")
    display_board()

from random import randrange   
def pc_mv():
    '''return pc move and marked on board'''
    global board
    pc_mv=randrange(1,space_num+1)
    while board[pc_mv-1]!='_':
        pc_mv=randrange(1,space_num+1)
    if board[pc_mv-1]=='_':
        board=board[:pc_mv-1]+board[pc_mv-1].replace('_','O')+board[pc_mv:]
    return board

def play_game():
    '''define a winner from game'''
    while True:
      player_mv()
      if 'XXX' in board:
        display_board()
        print('player wins')
        return False
      else:
        pc_mv()
        if 'OOO' in board:
          display_board()
          print('pc wins')
          return False
        else:
          display_board()
          if '_' not in board:
            print('No one wins')
            return False

start_game()
while True:
    play_game()
    result=input('wanna play again?')
    if result=='yes':
      board='_'*space_num
      display_board()
    elif result=='no':
      print('ok bye')
      break
    else:
      print('please answer yes or no')