from os import stat
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
    array.roll.points

