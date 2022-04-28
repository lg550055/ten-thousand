from collections import Counter
from random import randint

class GameLogic:
  # def __init__(self, roll):
  #   self.roll = roll

  

  @staticmethod
  def validate_keepers(roll, keepers):
    roll_list = list(roll)
    for k in keepers:
      if k not in roll_list:
        return False
      roll_list.remove(k)
    return True

  @staticmethod
  def roll_dice(n):
    temp = []
    for i in range(n):
      temp.append(randint(1,6))
    return tuple(temp)

  @staticmethod
  def calculate_score(roll):
    score = 0
    pairs = 0
    c = Counter(roll)
    if len(c) == 6:
      return 1500

    for number_rolled in c:
      if c[number_rolled] >= 3:
        if number_rolled == 1:
          score += (number_rolled * 100 * (c[number_rolled] - 2)) * 10
        else:
          score += number_rolled * 100 * (c[number_rolled] - 2)
      if c[number_rolled] == 2:
        if number_rolled == 1:
          score += 200
          pairs += 1
          if pairs == 3:
            return 1500
        elif number_rolled == 5:
          score += 100
          pairs += 1
          if pairs == 3:
            return 1500
        else:
            pairs += 1
            if pairs == 3:
              return 1500
      if c[number_rolled] == 1 and number_rolled == 1:
        score += 100
      elif c[number_rolled] == 1 and number_rolled == 5:
        score += 50
    return score


  @staticmethod
  def get_scorers(roll):
    scorers = []
    roll_score = GameLogic.calculate_score(roll)
    
    for i in range(len(roll)):
      roll_without_i = tuple([roll[j] for j in range(len(roll)) if j != i])
      if roll_score != GameLogic.calculate_score(roll_without_i):
        scorers.append(roll[i])
    
    return tuple(scorers)
