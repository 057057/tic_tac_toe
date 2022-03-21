
from random import randrange

space_num=20
board='_'*space_num
player_mv=int(input('1-20 choose one number'))
while player_mv>space_num:
    print('you must choose within',space_num)
    player_mv=int(input('1-20 choose one number'))
if player_mv<=space_num:
   board=board[:player_mv-1]+board[player_mv-1].replace('_','X')+board[player_mv:]
else:
    print('be good ok?')
print(board)

pc_mv=randrange(1,space_num+1)
while pc_mv==player_mv:
    pc_mv=randrange(1,space_num+1)
if pc_mv!=player_mv:
   board=board[:pc_mv-1]+board[pc_mv-1].replace('_','O')+board[pc_mv:]
   print(board)

for i in range(6):

space='_'*20
m_x=int(input('1-5 choose one'))
round_1_x=space[:m_x-1]+space[m_x-1].replace('_','X')+space[m_x:]
print(round_1_x)
m_o=int(input('1-5 choose one'))
round_1_o=round_1_x[:m_o-1]+round_1_x[m_o-1].replace('_','O')+round_1_x[m_o:]
print(round_1_o)