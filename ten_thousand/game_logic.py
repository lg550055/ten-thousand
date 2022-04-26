from collections import Counter
import random

class GameLogic:
  # def __init__(self,n):
  #   self.n = n

  @staticmethod
  def roll_dice(n):
    temp = []
    for i in range(n):
      temp.append(random.randint(1,6))
    return tuple(temp)

  @staticmethod
  def calculate_score(roll):
    score = 0
    c = Counter(roll)
    if len(c) == 6:
      return 1500
    # if len(c[2]) == 2:
    for number_rolled in c:
      if c[number_rolled] >= 3:
        if number_rolled == 1:
          return (number_rolled * 100 * (c[number_rolled] - 2)) * 10
        else:
          return number_rolled * 100 * (c[number_rolled] - 2)
    

