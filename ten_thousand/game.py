from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker

class Game:
  def __init__(self):
    pass

  def play(self, roller=GameLogic.roll_dice):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    prompt = input('> ')
    if prompt == 'n':
      print('OK. Maybe another time')
    else:
      turn = 1
      player1 = Banker()
      while True:
        dice = 6
        print(f'Starting round {turn}')
        print(f'Rolling {dice} dice...')
        roll_string = ''
        roll = roller(dice)
        for e in roll:
          roll_string += str(e) + ' '
        print(f'*** {roll_string}***')
        print('Enter dice to keep, or (q)uit:')
        prompt = input('> ')
        if prompt == 'q':
          break
        else:
          dice -= len(prompt)
          roll_tuple = tuple([int(ch) for ch in prompt])
          points = GameLogic.calculate_score(roll_tuple) # needs work
          player1.shelf(points)
          print(f'You have {player1.shelved} unbanked points and {dice} dice remaining')
          print('(r)oll again, (b)ank your points or (q)uit:')
          prompt = input('> ')
          if prompt == 'q':
            break
          if prompt == 'b':
            print(f'You banked {player1.shelved} points in round {turn}') # sub 1 for variable
            player1.bank()
            print(f'Total score is {player1.balance} points')
            turn += 1
      
      print(f'Thanks for playing. You earned {player1.balance} points')

if __name__ == "__main__":
  game = Game()
  game.play()