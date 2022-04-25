import random

class GameLogic():
  # def __init__():
    pass

@staticmethod
def roll_dice(n):
    temp = []
    for i in range(n):
      temp.append(random.randint(1,6))
    return tuple(temp)
