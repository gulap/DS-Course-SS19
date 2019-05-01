#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# type numbers 1-9 to play
# only choose empty fields
# type number 0 to restart
boardInit=" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "
board=boardInit
winner = False
while (winner==False):
  print(board)
  xMove=input('Player X where do you want to put? ')
  if xMove !='0':
    print('Your move is', xMove)
    board=board.replace(xMove, "X")
  else:
    print('Player O wins.')
    board=boardInit
  print(board)
  oMove=input('Player O where do you want to put? ')
  if oMove !='0':
    print('Your move is', oMove)
    board=board.replace(oMove, "O")
  else:
    print('Player X wins.')
    board=boardInit


# In[ ]:




