from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker

class Game:
  def __init__(self):
    pass

  def zilch(self, roll):
    print('****************************************')
    print('**        Zilch!!! Round over         **')
    print("****************************************")
    return GameLogic.calculate_score(roll)


  def play_round(self, player1, turn, roller):
    dice = 6
    print(f'Starting round {turn}')
    while dice:
      print(f'Rolling {dice} dice...')
      roll_string = ''
      roll = roller(dice)
      for e in roll:
        roll_string += str(e) + ' '

      valid_keepers = False
      while not valid_keepers:
        print(f'*** {roll_string}***')
        if not GameLogic.calculate_score(roll):
          print('****************************************')
          print('**        Zilch!!! Round over         **')
          print("****************************************")
          print(f'You banked 0 points in round {turn}')
          print(f'Total score is {player1.balance} points')
          return True
        print('Enter dice to keep, or (q)uit:')
        prompt = input('> ').replace(' ','')
        if prompt == 'q':
          return False
        keep_tuple = tuple([int(ch) for ch in prompt])
        valid_keepers = GameLogic.validate_keepers(roll, keep_tuple)
        if not valid_keepers:
          print('Cheater!!! Or possibly made a typo...')

      points = GameLogic.calculate_score(keep_tuple)
      player1.shelf(points)
      print(f'You have {player1.shelved} unbanked points and {dice-len(prompt)} dice remaining')
      if dice == len(prompt):
        dice = 6
      else:
        dice -= len(prompt)
      print('(r)oll again, (b)ank your points or (q)uit:')
      prompt = input('> ')
      if prompt == 'q':
        return False
      if prompt == 'b':
        print(f'You banked {player1.shelved} points in round {turn}')
        player1.bank()
        print(f'Total score is {player1.balance} points')
        return True

  def play(self, roller=GameLogic.roll_dice):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    prompt = input('> ')
    if prompt == 'n':
      print('OK. Maybe another time')
    else:
      turn = 1
      player1 = Banker()
      playing = True
      while playing:
        playing = self.play_round(player1, turn, roller)
        turn += 1
      print(f'Thanks for playing. You earned {player1.balance} points')

if __name__ == "__main__":
  game = Game()
  def fake_roller(dice):
    return (2,2,3,4,6,6)
  
  game.play()

