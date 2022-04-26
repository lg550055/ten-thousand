from telnetlib import GA
from urllib import response
from ten_thousand.game_logic import GameLogic

class Game:
  def __init__(self):
    pass

  def play(self, roller=GameLogic.roll_dice):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    response = input('> ')
    if response == 'n':
      print('OK. Maybe another time')
    else:    
      print('Starting round 1') # substitute 1 for variable
      print('Rolling 6 dice...') # substitute 6 for variable
      roll = ''
      for i in range(6):
        roll += str(roller(6)) + ' '
      print(f'*** {roll}***')
      print('Enter dice to keep, or (q)uit:')
      response = input('> ')
      if response == 'q':
        print('Thanks for playing. You earned 0 points') # substitute 0 for variable
